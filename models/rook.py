from models.piece import Piece

class Rook(Piece):
  def __init__(self, color, name, location) -> None:
    super().__init__(color, name, location)