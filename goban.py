#!/usr/bin/env python
# coding: utf-8

__author__ = "Aku Kotkavuo <aku@hibana.net>"
__version__ = "0.1"

import pygame
import go  # Import go.py, the Go library
from sys import exit

BACKGROUND = 'images/ramin.jpg'  # Background image for the board
BOARD_SIZE = (820, 820)  # Size of the game board
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Stone class derived from go.Stone to handle drawing in pygame
class Stone(go.Stone):
    def __init__(self, board, point, color):
        """Create, initialize and draw a stone."""
        super(Stone, self).__init__(board, point, color)
        self.coords = (5 + self.point[0] * 40, 5 + self.point[1] * 40)
        self.draw()

    def draw(self):
        """Draw the stone as a circle."""
        pygame.draw.circle(screen, self.color, self.coords, 20, 0)
        pygame.display.update()

    def remove(self):
        """Remove the stone from the board."""
        blit_coords = (self.coords[0] - 20, self.coords[1] - 20)
        area_rect = pygame.Rect(blit_coords, (40, 40))
        screen.blit(background, blit_coords, area_rect)
        pygame.display.update()
        super(Stone, self).remove()

# Board class derived from go.Board to handle drawing in pygame
class Board(go.Board):
    def __init__(self):
        """Create, initialize and draw an empty board."""
        super(Board, self).__init__()
        self.outline = pygame.Rect(45, 45, 720, 720)  # Outline of the board
        self.draw()

    def draw(self):
        """Draw the board to the background and blit it to the screen."""
        pygame.draw.rect(background, BLACK, self.outline, 3)  # Draw the board outline
        self.outline.inflate_ip(20, 20)  # Inflate the outline for future use as a collidebox for the mouse
        for i in range(18):
            for j in range(18):
                rect = pygame.Rect(45 + (40 * i), 45 + (40 * j), 40, 40)
                pygame.draw.rect(background, BLACK, rect, 1)  # Draw the grid
        for i in range(3):
            for j in range(3):
                coords = (165 + (240 * i), 165 + (240 * j))
                pygame.draw.circle(background, BLACK, coords, 5, 0)  # Draw hoshi points
        screen.blit(background, (0, 0))
        pygame.display.update()

    def update_liberties(self, added_stone=None):
        """Updates the liberties of the entire board, group by group."""
        for group in self.groups:
            if added_stone:
                if group == added_stone.group:
                    continue
            group.update_liberties()
        if added_stone:
            added_stone.group.update_liberties()

# Main game loop
def main():
    while True:
        pygame.time.wait(250)  # Wait to control the speed of the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and board.outline.collidepoint(event.pos):
                    x = int(round(((event.pos[0] - 5) / 40.0), 0))
                    y = int(round(((event.pos[1] - 5) / 40.0), 0))
                    stone = board.search(point=(x, y))
                    if stone:
                        stone.remove()
                    else:
                        added_stone = Stone(board, (x, y), board.turn())
                    board.update_liberties(added_stone)

# Entry point of the program
if __name__ == '__main__':
    pygame.init()
    # Set the window title
    pygame.display.set_caption('Goban')  
    # Set up the game window
    screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)  
    # Load the background image
    background = pygame.image.load(BACKGROUND).convert()  
    # Create an instance of the game board
    board = Board()  
    # Start the main game loop
    main()  
