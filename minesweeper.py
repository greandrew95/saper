import itertools
from random import sample

from bord import *


class Minesweeper(Bord):
    def __init__(self, width=10, height=10, count=5):
        super().__init__(width, height)
        a = sample([(i, j) for i in range(width) for j in range(height)], count)
        for x, y in a:
            self.board[x][y].state = -1

    def on_click(self, cell_coords):
        try:
            x, y = cell_coords
        except Exception:
            return
        if self.board[y][x].state == -2:
            self.board[y][x].state = sum(self.board[y + j][x + i].state == -1
                                         for i, j in itertools.product((-1, 0, 1), repeat=2)
                                         if 0 <= y + j < self.height and 0 <= x + i < self.width)
            if self.board[y][x].state == 0:
                for i, j in itertools.product((-1, 0, 1), repeat=2):
                    if 0 <= y + j < self.height and 0 <= x + i < self.width:
                        self.on_click((x + i, y + j))
