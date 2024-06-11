import pygame


class Cell():
    def __init__(self, state=-2, size=100):
        self.state = state
        self.size = size
        self.font = pygame.font.Font(None, size // 4)

    def render(self):
        renderSurface = pygame.Surface((self.size, self.size))
        if self.state == -1:
            renderSurface.fill((255, 0, 0))
        elif self.state != -2:
            renderSurface.fill((0, 0, 0))
            text = self.font.render(str(self.state), True, (0, 255, 0))
            renderSurface.blit(text, (self.size // 10, self.size // 10))
        pygame.draw.rect(renderSurface, (255, 255, 255), (0, 0, self.size, self.size), 2)
        return renderSurface

    def click(self):
        pass
