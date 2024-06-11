from minesweeper import *


def main():
    pygame.init()
    pygame.display.set_caption('Реакция на события от мыши')
    size = 520, 520
    screen = pygame.display.set_mode(size)
    minesweeper = Minesweeper(width=10, height=10)
    minesweeper.set_view(left=10, top=10, cell_size=50)

    running = True
    clock = pygame.time.Clock()
    fps = 30
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                minesweeper.get_click(event.pos)

        screen.fill((127, 127, 127))
        minesweeper.render(screen)
        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
