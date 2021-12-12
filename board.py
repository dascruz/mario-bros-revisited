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

    self.interfaz = clases.Interfaz()

    self.mario = clases.Mario(location=c.POS_MARIO)
    self.suelos = clases.Suelo(location=c.POS_DEFAULT)
    self.suelos.generar_suelo()

    self.enemigos = clases.Enemigo(location=c.POS_DEFAULT)

    self.bloques = clases.Bloque(location=c.POS_DEFAULT)
    self.bloques.generar_bloques()

    self.tuberias = clases.Tuberia(location=c.POS_DEFAULT)
    self.tuberias.generar_tuberias()

    self.nubes = clases.Nube(location=c.POS_DEFAULT)
    self.nubes.generar_nubes()

    self.arbustos = clases.Arbusto(location=c.POS_DEFAULT)
    self.arbustos.generar_arbustos()

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    
    self.mario.move()

    if self.mario.lives < 0:
      pyxel.quit()
    
    self.enemigos.generar_enemigos(pyxel.frame_count)
    self.enemigos.move()

    if self.interfaz.check_time():
      self.mario.lives -= 1

  def draw(self):
    # Rellenamos la pantalla de color azul
    pyxel.cls(6)

    # Dibujamos la interfaz
    self.interfaz.draw()

    # Dibujamos los objetos del juego
    self.suelos.dibujar_suelo()
    self.bloques.dibujar_bloques()
    self.tuberias.dibujar_tuberias()
    self.nubes.dibujar_nubes()
    self.arbustos.dibujar_arbustos()

    # Dibujamos a los enemigos
    self.enemigos.dibujar_enemigos()

    # Dibujamos a Mario
    self.mario.draw()

    # Código para debugging
    if self.mario.check_collision(self.bloques.bloques):
      text = "true"
    else:
      text = "false"
    pyxel.text(0, 0, text, 1)


Board()
