import pygame

from abc import abstractmethod
from pygame.surface import Surface

class Piece():
  def __init__(self, color: str, name: str, location: tuple) -> None:
    self.color = color
    self.name = name
    self.location = location
  
    self.piece = pygame.image.load(f"./images/pieces/{self.color}/{self.name}.png")
    self.piece = pygame.transform.scale(self.piece, (80,80))
  
  def get_location(self) -> tuple:
    return self.location
  
  def get_piece(self) -> Surface:
    return self.piece
  
  @abstractmethod
  def check(self) -> set:
    pass