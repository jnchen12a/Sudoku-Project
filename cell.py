# Cell Class
class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen
    self.sketched_value = 0

  def set_cell_value(self, value):
    self.value = value

  def set_sketched_value(self, value):
    self.sketched_value = value

  def draw(self): # FIXME: Finish this method
    main.py
    
  
  def sketch(self):
    pass

  def __repr__(self):
    return self.value