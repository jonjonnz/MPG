import pygame

width = 500
height = 500
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MPG-Test")
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = c
        self.velo = 10
        self.rect = (x, y, w, h)

    def draw(self,s):
        pygame.draw.rect(s, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.velo
        if keys[pygame.K_RIGHT]:
            self.x += self.velo
        if keys[pygame.K_UP]:
            self.y -= self.velo
        if keys[pygame.K_DOWN]:
            self.y += self.velo
        self.rect = (self.x,self.y,self.width,self.height)

def redraw_win(s,p):
    s.fill((255, 255, 255))
    p.draw(screen)
    pygame.display.update()


def main():
    run = True
    player = Player(50,50,100,100,(0,255,0))

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        redraw_win(screen,player)

main()