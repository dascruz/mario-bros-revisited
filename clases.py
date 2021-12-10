""" Archivo que contiene todos los objetos a usar en el videojuego
"""

import random, pyxel
import constantes as c

# Variable global utilizada para el movimiento de la cámara por el nivel
x_offset = 0


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
  
  # Método para dibujar en patalla el sprite
  def draw(self):
    pyxel.blt(self.x, self.y, self.img_bank, self.u, self.v,
              self.w, self.h, self.colkey)


class Mario(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(0, 0))
    self.lives = 3
    self.jumpCount = c.JUMP_HEIGHT
    self.isJump = False
  
  def move(self):
    # Lógica para el movimiento de Mario, comprobando que no se sale de los límites de la pantalla
    if pyxel.btn(pyxel.KEY_RIGHT) and self.x < (c.BOARD_WIDTH - self.w):
      if self.x < (c.BOARD_WIDTH / 2 - self.w):
        self.x = min(self.x + 2, c.BOARD_WIDTH - self.w)
      else:
       global x_offset
       x_offset += 2

    elif pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
      self.x = max(self.x - 2, 0)
    
    # Lógica para el salto de Mario, funciona como un movimiento parabólico en el eje Y
    if not (self.isJump):
      if pyxel.btn(pyxel.KEY_SPACE):
        self.isJump = True
    else: 
      if self.jumpCount >= -c.JUMP_HEIGHT:
        self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
        self.jumpCount -= 0.25
      else:
        self.jumpCount = c.JUMP_HEIGHT
        self.isJump = False


class Suelo(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(32, 0), colkey=-1)

  # Método para rellenar la pantalla con bloques de suelo
  def generar_suelo(self):
    self.suelo1 = [(i * c.UNIT - x_offset, int(c.BOARD_HEIGHT - c.UNIT * 1.5)) for i in range(c.UNIT * 4)]
    self.suelo2 = [(i * c.UNIT - x_offset, int(c.BOARD_HEIGHT - c.UNIT * 0.5)) for i in range(c.UNIT * 4)]

    for location in self.suelo1:
      suelo = Suelo(location)
      suelo.draw()
    
    for location in self.suelo2:
      suelo = Suelo(location)
      suelo.draw()


class Bloque(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(16, 0), colkey=-1)

  # Método para rellenar la pantalla con bloques de suelo
  def generar_bloques(self):
    altura = int(c.BOARD_HEIGHT - c.UNIT * 5.5)
    self.bloques = [(c.UNIT * 17 - x_offset, altura), (c.UNIT * 20 - x_offset, altura),
                    (c.UNIT * 21 - x_offset, altura), (c.UNIT * 22 - x_offset, altura),
                    (c.UNIT * 23 - x_offset, altura), (c.UNIT * 24 - x_offset, altura)]

    for location in self.bloques:
      bloque = Bloque(location)
      bloque.draw()

class Tuberia(Sprite):
  def __init__():
    Sprite.__init__()


class Interfaz:
  def __init__(self):
    self.score = 0
    self.time = 400
    self.coins = 0
  

  def draw_ui(self):
    pass


  def check_time(self):
    pass
