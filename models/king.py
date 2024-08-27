from models.piece import Piece

class King(Piece):
  def __init__(self, color, name, location) -> None:
    super().__init__(color, name, location)