import random, pyxel

# Clase principal que heredan todos los objetos gráficos del juego
class Sprite:
  def __init__(self, x: int, y: int, img: int, u: int, v: int, w: int, h: int, colkey: int = -1):
      self.x = x
      self.y = y
      self.img = img
      self.u = u
      self.v = v
      self.w = w
      self.h = h
      self.colkey = colkey


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
  def __init__():
    Sprite.__init__()


class Bloque(Sprite):
  def __init__():
    Sprite.__init__()


class Tuberia(Sprite):
  def __init__():
    Sprite.__init__()