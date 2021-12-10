""" Archivo principal que ejecuta el juego
"""

import pyxel, random
import clases
import constantes as c


class Board:
  def __init__(self):
    # Resolución de la NES (256 x 240)
    pyxel.init(c.BOARD_WIDTH, c.BOARD_HEIGHT, caption=c.BOARD_NAME)
    pyxel.load("assets/mario.pyxres")

    self.mario = clases.Mario(location=(c.UNIT * 3, c.BOARD_HEIGHT - int(c.UNIT * 2.5)))

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    
    self.mario.move()

  def draw(self):
    # Rellenamos la pantalla de color azul
    pyxel.cls(12)

    # Dibujamos a Mario
    self.mario.draw()

    # Dibujamos el suelo
    clases.Suelo.generar_suelo(self)
    clases.Bloque.generar_bloques(self)

Board()
