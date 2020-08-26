import pygame
from network import Network
import pygbutton

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, (0, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


width = 500
height = 500
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MPG-Test")
clock = pygame.time.Clock()


def redraw_win(s):
    s.fill((255, 255, 255))
    draw_text(screen, 'hello', 30, 100, 100)
    pygame.display.update()


def main():
    run = True
    n = Network()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redraw_win(screen)


# main()


def main_screen():

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()






main_screen()
