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
    elif pyxel.btn(pyxel.KEY_RIGHT):
      self.mario.move('right')
    elif pyxel.btn(pyxel.KEY_LEFT):
      self.mario.move('left')

  def draw(self):
    pyxel.cls(12)
    self.mario.draw()
    clases.Suelo.generar_suelo(self)

Board()
