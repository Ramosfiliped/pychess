from models.piece import Piece

class Pawn(Piece):
  def __init__(self, color, piece) -> None:
    super().__init__(color, piece)