import pygame
import sys
from flappyBird import Game

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird - Menu")

font = pygame.font.Font("Arial.ttf", 70)
button_font = pygame.font.Font("Arial.ttf", 50)


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        pygame.draw.rect(surface, current_color, self.rect, border_radius=15)

        text_surface = button_font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


def menu():
    play_button = Button(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50, 300, 100, "PLAY", (216, 210, 210), (182, 175, 175))
    quit_button = Button(SCREEN_WIDTH / 2 - 150, (SCREEN_HEIGHT / 2 - 50) + 150, 300, 100, "QUIT", (216, 210, 210), (182, 175, 175))
    background = pygame.image.load("asset/background.jpg").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


    running = True

    while running:
        window.blit(background, (0, 0))

        title = font.render("FLAPPY BIRD", True, (0, 0, 0))
        window.blit(title, (300, 150))

        play_button.draw(window)
        quit_button.draw(window)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()

            if play_button.is_clicked(event):
                game = Game()
                game.run()

            if quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    menu()
