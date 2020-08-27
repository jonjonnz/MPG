import pygame
from network import Network
import pygbutton
import os

# Default Screen size
width = 800
height = 600

# Folder Structures for images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
bg_img_folder = os.path.join(img_folder, "background")

# Load images
background_img = pygame.image.load(os.path.join(bg_img_folder, "mainscreen.jpg"))
background_img = pygame.transform.scale(background_img, (width, height))

# Button Defaults
button_row = 465
button_column = 100
button_color = (0, 200, 0)

# Initialization and creating a window
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MPG-Test")
clock = pygame.time.Clock()


def draw_main_screen(s, buttons):
    """Updating everything on main screen in while loop with single function"""
    s.blit(background_img, [0, 0])
    draw_text(screen, 'BlackJack', 100, 300, 75, (234, 235, 23))
    for button in buttons:
        button.draw(s)
    pygame.display.update()


def draw_text(surf, text, size, x, y, color):
    """Draw text on surface"""
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def main_screen():
    """Main screen loop"""

    while True:
        clock.tick(60)

        # Buttons for game to connect to a new game or an existing one
        new_game_button = pygbutton.PygButton((button_column, button_row, 100, 50), 'New Game', button_color)
        existing_game_button = pygbutton.PygButton((button_column + 200, button_row, 100, 50), 'Join Existing', button_color)
        quit_game_button = pygbutton.PygButton((button_column + 400, button_row, 100, 50), 'Quit', button_color)
        buttons = [new_game_button, existing_game_button, quit_game_button]

        # Checking for event on the main screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw_main_screen(screen, buttons)


main_screen()
