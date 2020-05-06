import pygame
import sys
import time


class Game:
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 450

        self.fps_controller = pygame.time.Clock()

        self.score = 0

    def init_and_check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()

    def set_surface_and_title(self):
        self.play_surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))
        pygame.display.set_caption('mySnake-V2.0')
        pygame.mixer.music.load('Mitch Murder - Hollywood Heights.mp3')
        pygame.mixer.music.play(-1)

    def event_loop(self, change_to):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to

    def refresh_screen(self):
        pygame.display.flip()
        self.fps_controller.tick(5)

    def show_score(self, choice=1):
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, (0, 0, 0))
        s_rect = s_surf.get_rect()
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (self.screen_width // 2, self.screen_height // 2)
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, (255, 0, 0))
        go_rect = go_surf.get_rect()
        go_rect.midtop = (self.screen_width // 2, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        pygame.mixer.music.stop()
        time.sleep(3)
        pygame.quit()
        sys.exit()
