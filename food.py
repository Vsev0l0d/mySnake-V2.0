import pygame
import random


class Food:
    def __init__(self, screen_width, screen_height, snake_body):
        self.food_surf = pygame.image.load('pizza.png')
        self.food_pos = [random.randrange(1, screen_width // 30) * 30,
                         random.randrange(1, screen_height // 30) * 30]
        for pos in snake_body:
            while (abs(pos[0] - self.food_pos[0]) < 30 and
                   abs(pos[1] - self.food_pos[1]) < 30):
                self.food_pos = [random.randrange(1, screen_width // 30) * 30,
                                 random.randrange(1, screen_height // 30) * 30]

    def draw_food(self, play_surface):
        play_surface.blit(self.food_surf, (self.food_pos[0], self.food_pos[1]))
