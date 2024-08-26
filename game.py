import pygame

WIDTH = 800
HEIGHT = 800

turn_step = 0

class Chess:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Two-Player Chess Game')
        icon = pygame.image.load("./images/logo.jpg")
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.timer = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.medium_font = pygame.font.Font('freesansbold.ttf', 40)
        self.big_font = pygame.font.Font('freesansbold.ttf', 50)

    def main_loop(self) -> None:
        fps = 60
        run = True
        while run:
            self.timer.tick(fps)
            self.draw_board()
            pygame.display.flip()
        pygame.quit()

    def draw_board(self):
        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(
                    surface=self.screen, 
                    color='light gray', 
                    rect=[600 - (column * 200), row * 100, 100, 100]
                )
            else:
                pygame.draw.rect(
                    surface=self.screen, 
                    color='light gray', 
                    rect=[700 - (column * 200), row * 100, 100, 100]
                )

            pygame.draw.rect(
              surface=self.screen, 
              color='gray', 
              rect=[0, 800, WIDTH, 100]
            )

            pygame.draw.rect(
              surface=self.screen, 
              color='gold', 
              rect=[0, 800, WIDTH, 100], 
              width=5
            )

            pygame.draw.rect(
              surface=self.screen, 
              color='gold', 
              rect=[800, 0, 200, HEIGHT], 
              width=5
            )

            status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                        'Black: Select a Piece to Move!', 'Black: Select a Destination!']

            self.screen.blit(self.big_font.render(

                status_text[turn_step], True, 'black'), (20, 820))

            for i in range(9):

                pygame.draw.line(self.screen, 'black', (0, 100 * i), (800, 100 * i), 2)

                pygame.draw.line(self.screen, 'black', (100 * i, 0), (100 * i, 800), 2)

            self.screen.blit(self.medium_font.render('FORFEIT', True, 'black'), (810, 830))