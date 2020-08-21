import pygame


class Player:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = c
        self.velo = 10
        self.rect = (x, y, w, h)

    def draw(self, s):
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
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
