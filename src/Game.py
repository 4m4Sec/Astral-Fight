from lib.manager.EntityManager import EntityManager
from src.entity.Player import Player
import pygame

class Game():

    def __init__(self):
        self.entity_manager = EntityManager()
        self.player = Player()
        self.running = True
        self.create_window()

    def is_running(self):
        return self.running

    def set_running(self, value):
        self.running = value

    def create_window(self):
        pygame.display.set_caption("Astral-Fight | Shoot the aliens !")
        self.background = pygame.image.load("src/assets/background.jpg")
        self.screen = pygame.display.set_mode((1500, 800))

    def display_screen(self):
        self.screen.blit(self.background, (0, -200))

    def display_player(self):
        self.screen.blit(self.player.image, self.player.rect)

    def display_projectiles(self):
        for projectiles in self.entity_manager.get_projectiles():
            if projectiles.get_position().get_y() > 0:
                self.screen.blit(projectiles.image, projectiles.rect)
            else:
                self.entity_manager.projectiles.remove(projectiles)

    def display_aliens(self):
        for aliens in self.entity_manager.get_aliens():
            self.screen.blit(aliens.image, aliens.rect)

    def update_screen(self):
        pygame.display.flip()

    def update_all(self):
        self.display_screen()
        self.display_player()
        self.display_projectiles()
        self.display_aliens()
        self.update_screen()