import pygame

from cell import Cell


class Bord:
    def __init__(self, width=3, height=3):
        self.cell_size = None
        self.top = None
        self.left = None
        self.width = width
        self.height = height
        self.board = [[Cell() for x in range(width)] for y in range(height)]
        self.set_view()

    def set_view(self, left=0, top=0, cell_size=100):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        for row in self.board:
            for cell in row:
                cell.size = cell_size

    def render(self, screen):
        renderSurface = pygame.Surface((self.width * self.cell_size, self.height * self.cell_size))
        renderSurface.fill((0, 0, 0))
        for y in range(self.height):
            for x in range(self.width):
                renderSurface.blit(self.board[y][x].render(), (x * self.cell_size, y * self.cell_size))
        screen.blit(renderSurface, (self.left, self.top))

    def get_cell(self, mouse_pos):
        xm, ym = mouse_pos
        xm -= self.left
        ym -= self.top
        x, y = xm / self.cell_size, ym / self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return int(x), int(y)
        return None

    def on_click(self, cell_coords):
        try:
            x, y = cell_coords
        except Exception:
            return

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
