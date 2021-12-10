import random, pyxel

import constantes as c
# Clase principal que heredan todos los objetos gráficos del juego
class Sprite:
  def __init__(self, location: tuple, img_bank: int, uv: tuple, size=(c.UNIT, c.UNIT), colkey=0):
    self.x = location[0]
    self.y = location[1]
    self.img_bank = img_bank
    self.u = uv[0]
    self.v = uv[1]
    self.w = size[0]
    self.h = size[1]
    self.colkey = colkey
  
  def draw(self):
    pyxel.blt(self.x, self.y, self.img_bank, self.u, self.v,
              self.w, self.h, self.colkey)

class Interfaz:
  def __init__(self):
    self.score = 0
    self.time = 400
    self.coins = 0
  

  def draw_ui(self):
    pass


  def check_time(self):
    pass


class Mario(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(0, 0))
    self.lives = 3
  
  def move(self, direction: str):
    """ This is an example of a method that moves Mario, it receives the
    direction and the size of the board """
    # Checking the current horizontal size of Mario to stop him before
    # he reaches the right border
    if direction.lower() == 'right' and self.x < (c.BOARD_WIDTH - self.w):
      self.x = min(self.x + 2, c.BOARD_WIDTH - self.w)
    elif direction.lower() == 'left' and self.x > 0:
      # I am assuming that if it is not right it will be left
      self.x = max(self.x - 2, 0)


class Suelo(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(32, 0), colkey=-1)

  def generar_suelo(self):
    self.suelo1 = [(i * c.UNIT, int(c.BOARD_HEIGHT - c.UNIT * 1.5)) for i in range(c.UNIT * 4)]
    self.suelo2 = [(i * c.UNIT, int(c.BOARD_HEIGHT - c.UNIT * 0.5)) for i in range(c.UNIT * 4)]

    for location in self.suelo1:
      suelo = Suelo(location)
      suelo.draw()
    
    for location in self.suelo2:
      suelo = Suelo(location)
      suelo.draw()

class Tuberia(Sprite):
  def __init__():
    Sprite.__init__()