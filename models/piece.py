import pygame

from abc import abstractmethod

class Piece():
  def __init__(self, color, name) -> None:
    self.color = color
    self.name = name
  
    self.piece = pygame.image.load(f"./images/pieces/{self.color}/{self.piece}.png")
    self.piece = pygame.transform.scale(self.piece, (80,80))
  
  