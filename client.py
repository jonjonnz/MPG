import pygame
from network import Network
import pygbutton
import os

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


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
    # Buttons for game to connect to a new game or an existing one
    new_game_button = pygbutton.PygButton((button_column, button_row, 100, 50), 'New Game', button_color)
    existing_game_button = pygbutton.PygButton((button_column, button_row + 75, 100, 50), 'Join Existing', button_color)
    quit_game_button = pygbutton.PygButton((button_column, button_row + 150, 100, 50), 'Quit', button_color)
    buttons = {'new': new_game_button, 'existing': existing_game_button, 'quit': quit_game_button}
    run = True
    while run:
        clock.tick(60)
        # Checking for event on the main screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if 'click' in buttons['new'].handleEvent(event):
                start_new_game()
            elif 'click' in buttons['existing'].handleEvent(event):
                join_existing_game()
            elif 'click' in buttons['quit'].handleEvent(event):
                run = False

        draw_main_screen(screen, buttons.values())
    pygame.quit()


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
button_row = 100
button_column = 100
button_color = (0, 200, 0)

# Initialization and creating a window
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MPG-Test")
clock = pygame.time.Clock()

main_screen()


# def main():
#     clock = pygame.time.Clock()
#     input_box1 = InputBox(100, 100, 140, 32)
#     input_box2 = InputBox(100, 300, 140, 32)
#     input_boxes = [input_box1, input_box2]
#     done = False
#
#     while not done:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#             for box in input_boxes:
#                 box.handle_event(event)
#
#         for box in input_boxes:
#             box.update()
#
#         screen.fill((30, 30, 30))
#         for box in input_boxes:
#             box.draw(screen)
#
#         pygame.display.flip()
#         clock.tick(30)
