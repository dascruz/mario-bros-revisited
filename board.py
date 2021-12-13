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

    # Inicializamos y generamos todos los objetos del juego
    self.interfaz = clases.Interfaz()
    self.mario = clases.Mario()
    self.enemigos = clases.Enemigo()
    self.suelo = clases.Generador.generar_objetos(self, c.SUELO, clases.Suelo)
    self.bloques_ladrillo = clases.Generador.generar_objetos(self, c.BLOQUES_LADRILLO, clases.BloqueLadrillo)
    self.bloques_objeto = clases.Generador.generar_objetos(self, c.BLOQUES_OBJETO, clases.BloqueObjeto)
    self.bloques_moneda = clases.Generador.generar_objetos(self, c.BLOQUES_MONEDA, clases.BloqueMoneda)
    self.tuberias = clases.Generador.generar_objetos(self, c.TUBERIAS, clases.Tuberia)
    self.nubes = clases.Generador.generar_objetos(self, c.NUBES, clases.Nube)
    self.arbustos = clases.Generador.generar_objetos(self, c.ARBUSTOS, clases.Arbusto)
    self.colisiones = self.bloques_ladrillo + self.bloques_moneda + self.bloques_objeto + self.tuberias

    pyxel.run(self.update, self.draw)

  def update(self):
    # Tecla ESC para salir del juego
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    
    # Comprobamos entrada del usuario en cada frame para mover a Mario
    self.mario.move(self.colisiones)

    # EL juego se cierra automáticamente si nos quedamos sin vidas
    if self.mario.lives < 0:
      pyxel.quit()
    
    # Los enemigos se generan cada 3-5 segundos y se dirigen hacia nosotros
    self.enemigos.generar_enemigos(pyxel.frame_count)
    self.enemigos.move(self.colisiones)

    # Mario pierde una vida si acaba el tiempo
    if self.interfaz.check_time(pyxel.frame_count):
      self.mario.lives -= 1

  def draw(self):
    # Rellenamos la pantalla de color azul
    pyxel.cls(6)

    # Dibujamos la interfaz
    self.interfaz.draw()

    # Dibujamos los objetos del juego
    clases.Generador.dibujar_objetos(self, self.suelo)
    clases.Generador.dibujar_objetos(self, self.bloques_ladrillo)
    clases.Generador.dibujar_objetos(self, self.bloques_objeto)
    clases.Generador.dibujar_objetos(self, self.bloques_moneda)
    clases.Generador.dibujar_objetos(self, self.tuberias)
    clases.Generador.dibujar_objetos(self, self.nubes)
    clases.Generador.dibujar_objetos(self, self.arbustos)

    # Dibujamos a los enemigos
    self.enemigos.dibujar_enemigos()

    # Dibujamos a Mario
    self.mario.draw()


Board()
