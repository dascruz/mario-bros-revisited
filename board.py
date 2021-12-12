""" Archivo principal que ejecuta el juego
"""

import pyxel, random
import clases
import constantes as c


class Board:
  def __init__(self):
    # Inciamos el motor Pyxel y cargamos el banco de imágenes
    pyxel.init(c.BOARD_WIDTH, c.BOARD_HEIGHT, caption=c.BOARD_NAME, fps=c.FPS)
    pyxel.load("assets/mario.pyxres")
    pyxel.frame_count

    self.interfaz = clases.Interfaz()

    self.mario = clases.Mario(location=c.POS_MARIO)
    self.suelos = clases.Suelo((0, 0))
    self.suelos.generar_suelo()

    self.bloques = clases.Bloque((0, 0))
    self.bloques.generar_bloques()

    self.tuberias = clases.Tuberia((0, 0))
    self.tuberias.generar_tuberias()

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    
    self.mario.move()
    if self.mario.lives < 0:
      pyxel.quit()

    if self.interfaz.check_time():
      self.mario.lives -= 1

  def draw(self):
    # Rellenamos la pantalla de color azul
    pyxel.cls(12)
    # Dibujamos la interfaz
    self.interfaz.draw()

    # Dibujamos a Mario
    self.mario.draw()

    # Dibujamos los objetos del juego
    self.suelos.dibujar_suelo()
    self.bloques.dibujar_bloques()
    self.tuberias.dibujar_tuberias()


    pyxel.text(0, 0, str(self.mario.y), 1)


Board()
