import pygame
import random
from math import hypot


class Snake:
    def __init__(self):
        self.snake_head_pos = [90, 60]
        self.snake_body = [[90, 60], [60, 60], [30, 60]]
        self.scales_surf = pygame.image.load('scales.png')
        self.direction = "RIGHT"
        self.change_to = self.direction
        self.is_the_head_in_the_field = True

    def validate_direction_and_change(self):
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            if self.is_the_head_in_the_field:
                self.direction = self.change_to

    def change_head_position(self):
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 30
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 30
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 30
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 30

    def snake_body_mechanism(self, score, food_pos, screen_width, screen_height):
        self.snake_body.insert(0, list(self.snake_head_pos))
        if (hypot(self.snake_head_pos[0] - food_pos[0],
                  self.snake_head_pos[1] - food_pos[1]) < 30):
            while True:
                check = True
                for pos in self.snake_body:
                    if hypot(pos[0] - food_pos[0],
                             pos[1] - food_pos[1]) < 30:
                        check = False
                        food_pos = [random.randrange(1, screen_width // 30) * 30,
                                    random.randrange(1, screen_height // 30) * 30]
                if check:
                    break
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos

    def draw_snake(self, play_surface, screen_width, screen_height):
        background_surf = pygame.image.load('grass.bmp')
        background_surf = pygame.transform.scale(background_surf, (screen_width, screen_height))
        play_surface.blit(background_surf, (0, 0))
        for pos in self.snake_body:
            play_surface.blit(self.scales_surf, pos)

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        if self.snake_head_pos[0] > screen_width - 30:
            self.is_the_head_in_the_field = False
            self.snake_head_pos[0] = -30
        elif (self.snake_head_pos[0] < 30) & (self.snake_head_pos[0] != 0):
            self.is_the_head_in_the_field = False
            self.snake_head_pos[0] = screen_width
        elif self.snake_head_pos[1] > screen_height - 30:
            self.is_the_head_in_the_field = False
            self.snake_head_pos[1] = -30
        elif (self.snake_head_pos[1] < 30) & (self.snake_head_pos[1] != 0):
            self.is_the_head_in_the_field = False
            self.snake_head_pos[1] = screen_height
        else:
            self.is_the_head_in_the_field = True
        for block in self.snake_body[1:]:
            if (hypot(self.snake_head_pos[0] - block[0],
                      self.snake_head_pos[1] - block[1]) < 30) & (hypot(self.snake_head_pos[0] - block[0],
                                                                        self.snake_head_pos[1] - block[1]) != 0):
                game_over()
