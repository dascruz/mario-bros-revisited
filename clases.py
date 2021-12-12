""" Archivo que contiene todos los objetos a usar en el videojuego
"""

import pyxel
import constantes as c

# Variable global utilizada para el movimiento de la cámara por el nivel
x_offset = 0


# Clase principal que heredan todos los objetos gráficos del juego
class Sprite:
  # Inicializamos la posición y cargamos el sprite correspondiente del banco de imágenes
  def __init__(self, location, img_bank: int, uv: tuple, size=(c.UNIT, c.UNIT), colkey=0):
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
    pyxel.blt(self.x - x_offset, self.y, self.img_bank, self.u, self.v,
              self.w, self.h, self.colkey)


class Mario(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(0, 0))
    self.lives = 3
    self.jumpCount = c.JUMP_HEIGHT
    self.isJump = False
  
  def move(self):
    # Lógica para el movimiento de Mario, comprobando que no se sale de los límites de la pantalla
    global x_offset

    if pyxel.btn(pyxel.KEY_RIGHT):
      if self.x > (c.UNIT * 5 + x_offset):
        x_offset += c.SPEED

      self.x = self.x + c.SPEED
    elif pyxel.btn(pyxel.KEY_LEFT):
      self.x = max(self.x - c.SPEED, 0 + x_offset)
    
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
    self.suelos = []

  # Método para rellenar la pantalla con bloques de suelo
  def generar_suelo(self):
    for location in c.SUELO:
      suelo = Suelo(location)
      self.suelos.append(suelo)
    
  def dibujar_suelo(self):
    for suelo in self.suelos:
      suelo.draw()


class Bloque(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(16, 0), colkey=-1)
    self.bloques = []

  # Método para colocar los bloques
  def generar_bloques(self):
    for location in c.BLOQUES:
      bloque = Bloque(location)
      self.bloques.append(bloque)
  
  def dibujar_bloques(self):
    for bloque in self.bloques:
      bloque.draw()

class Tuberia(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(109, 0))
    self.tuberias = []
  
  # Método para colocar las tuberías
  def generar_tuberias(self):
    for location in c.TUBERIAS:
      tuberia = Tuberia(location)
      self.tuberias.append(tuberia)
  
  def dibujar_tuberias(self):
    for tuberia in self.tuberias:
      tuberia.draw()


# Objeto que controla la interfaz del juego, incluyendo la puntuación y las monedas recogidas
class Interfaz:
  def __init__(self):
    self.score = 0
    self.time = c.TIME
    self.coins = 0
    self.counter = 0

  def draw(self):
    altura1 = c.UNIT * 1.5
    altura2 = c.UNIT * 2

    # Puntuación
    pyxel.text(c.UNIT * 2, altura1, "MARIO", 7)
    pyxel.text(c.UNIT * 2, altura2, f"{self.score:06d}", 7)

    # Monedas
    # pyxel.blt()
    pyxel.text(c.UNIT * 5, altura2, "x " + f"{self.coins:02d}", 7)

    # Nivel
    pyxel.text(c.UNIT * 9, altura1, "WORLD", 7)
    pyxel.text(c.UNIT * 9.3, altura2, "1-1", 7)

    # Tiempo
    pyxel.text(c.UNIT * 13, altura1, "TIME", 7)
    pyxel.text(c.UNIT * 13.3, altura2, f"{self.time:03d}", 7)

  # Método encargado del tiempo de ejecución del juego
  def check_time(self):
    self.counter += 1
    # Un segundo equivale a 60 fotogramas
    if self.counter % c.FPS == 0:
      self.time -= 1

    if self.time < 0:
      self.time = c.TIME
      return True
    
    return False
  

  # Método llamado cuando Mario recoge una moneda
  def add_coin(self):
    self.coins += 1
