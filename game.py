import pygame

from enum import Enum
from models.pawn import Pawn
from models.rook import Rook
from models.king import King
from models.queen import Queen
from models.bishop import Bishop
from models.knight import Knight

WIDTH = 800
HEIGHT = 800

turn_step = 0

class Color(Enum):
    WHITE = 'white'
    BLACK = 'black'

class Chess:
  def __init__(self) -> None:
    pygame.init()
    pygame.display.set_caption('PyChess')
    icon = pygame.image.load("./images/logo.jpg")
    pygame.display.set_icon(icon)
    self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
    self.timer = pygame.time.Clock()
    self.font = pygame.font.Font('freesansbold.ttf', 20)
    self.medium_font = pygame.font.Font('freesansbold.ttf', 40)
    self.big_font = pygame.font.Font('freesansbold.ttf', 50)

  def draw_board(self):
    for row in range(8):
      for column in range(8):
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

        status_text = [
          'White: Select a Piece to Move!', 'White: Select a Destination!',
          'Black: Select a Piece to Move!', 'Black: Select a Destination!'
        ]

        self.screen.blit(
          source=self.big_font.render(
            status_text[turn_step], 
            True, 
            'black'
          ), 
          dest=(20, 820)
        )

        for i in range(9):
          pygame.draw.line(self.screen, 'black', (0, 100 * i), (800, 100 * i), 2)
          pygame.draw.line(self.screen, 'black', (100 * i, 0), (100 * i, 800), 2)

        self.screen.blit(self.medium_font.render('FORFEIT', True, 'black'), (810, 830))

  def create_white_pieces(self):
    for i in range(8):
      pawn = Pawn(
        color=Color.WHITE.value,
        name='pawn',
        location=(i,1)
      )
      self.screen.blit(
        source=pawn.get_piece(),
        dest=(pawn.get_location()[0] * 100 + 10, pawn.get_location()[1] * 100 + 30)
      )
    
    rook = Rook(
      color=Color.WHITE.value,
      name='rook',
      location=(0,0)
    )
    self.screen.blit(
      source=rook.get_piece(),
      dest=(rook.get_location()[0] * 100 + 10, rook.get_location()[1] * 100 + 30)
    )
    
    rook = Rook(
      color=Color.WHITE.value,
      name='rook',
      location=(7,0)
    )
    self.screen.blit(
      source=rook.get_piece(),
      dest=(rook.get_location()[0] * 100 + 10, rook.get_location()[1] * 100 + 30)
    )
    
    bishop = Bishop(
      color=Color.WHITE.value,
      name='bishop',
      location=(6,0)
    )
    self.screen.blit(
      source=bishop.get_piece(),
      dest=(bishop.get_location()[0] * 100 + 10, bishop.get_location()[1] * 100 + 30)
    )
    
    bishop = Bishop(
      color=Color.WHITE.value,
      name='bishop',
      location=(2,0)
    )
    self.screen.blit(
      source=bishop.get_piece(),
      dest=(bishop.get_location()[0] * 100 + 10, bishop.get_location()[1] * 100 + 30)
    )

    knight = Knight(
      color=Color.WHITE.value,
      name='knight',
      location=(5,0)
    )
    self.screen.blit(
      source=knight.get_piece(),
      dest=(knight.get_location()[0] * 100 + 10, knight.get_location()[1] * 100 + 30)
    )
    
    knight = Knight(
      color=Color.WHITE.value,
      name='knight',
      location=(1,0)
    )
    self.screen.blit(
      source=knight.get_piece(),
      dest=(knight.get_location()[0] * 100 + 10, knight.get_location()[1] * 100 + 30)
    )

    bishop = Bishop(
      color=Color.WHITE.value,
      name='bishop',
      location=(2,0)
    )
    self.screen.blit(
      source=bishop.get_piece(),
      dest=(bishop.get_location()[0] * 100 + 10, bishop.get_location()[1] * 100 + 30)
    )
    
    king = King(
      color=Color.WHITE.value,
      name='king',
      location=(3,0)
    )
    self.screen.blit(
      source=king.get_piece(),
      dest=(king.get_location()[0] * 100 + 10, king.get_location()[1] * 100 + 30)
    )
    
    queen = Queen(
      color=Color.WHITE.value,
      name='queen',
      location=(4,0)
    )
    self.screen.blit(
      source=queen.get_piece(),
      dest=(queen.get_location()[0] * 100 + 10, queen.get_location()[1] * 100 + 30)
    )

  def create_black_pieces(self):
    for i in range(8):
      pawn = Pawn(
        color=Color.BLACK.value,
        name='pawn',
        location=(i,6)
      )
      self.screen.blit(
        source=pawn.get_piece(),
        dest=(pawn.get_location()[0] * 100 + 10, pawn.get_location()[1] * 100 + 30)
      )
    
    rook = Rook(
      color=Color.BLACK.value,
      name='rook',
      location=(0,7)
    )
    self.screen.blit(
      source=rook.get_piece(),
      dest=(rook.get_location()[0] * 100 + 10, rook.get_location()[1] * 100 + 30)
    )
    
    rook = Rook(
      color=Color.BLACK.value,
      name='rook',
      location=(7,7)
    )
    self.screen.blit(
      source=rook.get_piece(),
      dest=(rook.get_location()[0] * 100 + 10, rook.get_location()[1] * 100 + 30)
    )
    
    bishop = Bishop(
      color=Color.BLACK.value,
      name='bishop',
      location=(6,7)
    )
    self.screen.blit(
      source=bishop.get_piece(),
      dest=(bishop.get_location()[0] * 100 + 10, bishop.get_location()[1] * 100 + 30)
    )
    
    bishop = Bishop(
      color=Color.BLACK.value,
      name='bishop',
      location=(2,7)
    )
    self.screen.blit(
      source=bishop.get_piece(),
      dest=(bishop.get_location()[0] * 100 + 10, bishop.get_location()[1] * 100 + 30)
    )

    knight = Knight(
      color=Color.BLACK.value,
      name='knight',
      location=(5,7)
    )
    self.screen.blit(
      source=knight.get_piece(),
      dest=(knight.get_location()[0] * 100 + 10, knight.get_location()[1] * 100 + 30)
    )
    
    knight = Knight(
      color=Color.BLACK.value,
      name='knight',
      location=(1,7)
    )
    self.screen.blit(
      source=knight.get_piece(),
      dest=(knight.get_location()[0] * 100 + 10, knight.get_location()[1] * 100 + 30)
    )

    bishop = Bishop(
      color=Color.BLACK.value,
      name='bishop',
      location=(2,7)
    )
    self.screen.blit(
      source=bishop.get_piece(),
      dest=(bishop.get_location()[0] * 100 + 10, bishop.get_location()[1] * 100 + 30)
    )
    
    king = King(
      color=Color.BLACK.value,
      name='king',
      location=(3,7)
    )
    self.screen.blit(
      source=king.get_piece(),
      dest=(king.get_location()[0] * 100 + 10, king.get_location()[1] * 100 + 30)
    )
    
    queen = Queen(
      color=Color.BLACK.value,
      name='queen',
      location=(4,7)
    )
    self.screen.blit(
      source=queen.get_piece(),
      dest=(queen.get_location()[0] * 100 + 10, queen.get_location()[1] * 100 + 30)
    )

  def main_loop(self) -> None:
    fps = 60
    run = True
    while run:
      self.timer.tick(fps)
      self.screen.fill('dark gray')

      self.draw_board()
      self.create_white_pieces()
      self.create_black_pieces()

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False
      pygame.display.flip()
    pygame.quit()