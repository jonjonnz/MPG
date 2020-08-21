import pygame
from network import Network
from player import Player

width = 500
height = 500
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MPG-Test")
clock = pygame.time.Clock()


def redraw_win(s, p, p2):
    s.fill((255, 255, 255))
    p.draw(screen)
    p2.draw(screen)
    pygame.display.update()


def main():
    run = True
    n = Network()
    player = n.get_client()
    while run:
        clock.tick(60)
        player2 = n.send(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        redraw_win(screen, player, player2)


main()
