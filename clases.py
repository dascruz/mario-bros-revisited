""" Archivo que contiene todos los objetos a usar en el videojuego
"""

import pyxel, random
import constantes as c

# Variable global utilizada para el movimiento de la cámara por el nivel
x_offset = 0


# Clase principal que heredan todos los objetos gráficos del juego
class Sprite:
  # Inicializamos la posición y cargamos el sprite correspondiente del banco de imágenes
  def __init__(self, location, img_bank: int, uv: tuple, size=(c.UNIT, c.UNIT), colkey=6):
    self.x = location[0]
    self.y = location[1]
    self.img_bank = img_bank
    self.u = uv[0]
    self.v = uv[1]
    self.w = size[0]
    self.h = size[1]
    self.colkey = colkey
  
  # Método para comprobar colisiones con objetos
  def check_collision(self, objects):
    # Colisión AABB. Source: https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
    for object in objects:
      if (self.x < object.x + object.w and self.x + self.w > object.x and
        self.y < object.y + object.h and self.h + self.y > object.y):
        return True
    
    return False

  # Método para dibujar en patalla el sprite
  def draw(self):
    pyxel.blt(self.x - x_offset, self.y, self.img_bank, self.u, self.v,
              self.w, self.h, self.colkey)


class Mario(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=(80, 0))
    self.lives = 3
    self.jump_time = c.JUMP_HEIGHT
    self.jump_active = False
  
  def move(self):
    # Lógica para el movimiento de Mario, comprobando que no se sale de los límites de la pantalla
    # Movimiento horizontal con las teclas A y D
    global x_offset

    if pyxel.btn(pyxel.KEY_D):
      if self.x > (c.UNIT * 5 + x_offset):
        x_offset += c.SPEED

      self.x = self.x + c.SPEED
    elif pyxel.btn(pyxel.KEY_A):
      self.x = max(self.x - c.SPEED, 0 + x_offset)
    
    # Lógica para el salto de Mario, funciona como un movimiento parabólico en el eje Y
    if not (self.jump_active):
      if pyxel.btn(pyxel.KEY_SPACE):
        self.jump_active = True
    else: 
      if self.jump_time >= -c.JUMP_HEIGHT:
        self.y -= (self.jump_time * abs(self.jump_time)) * 0.5
        self.jump_time -= 0.25
      else:
        self.jump_time = c.JUMP_HEIGHT
        self.jump_active = False


class Enemigo(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=c.UV_GOOMBA)
    self.enemigos = []
    prob = random.uniform(0, 1)
    if prob < 0.25:
      self.u, self.v = c.UV_KOOPA
      self.h = 23
      self.tipo = "koopa"
    else:
      self.tipo = "goomba"
  
  def move(self):
    for enemigo in self.enemigos:
      enemigo.x -= c.ENEMY_SPEED

      # El enemigo aparece en el cielo para añadir variedad al movimiento (puede caer encima de un bloque por ejemplo)
      if enemigo.y + enemigo.h < c.UNIT * 14:
        enemigo.y += c.VELOCITY

      # Los enemigos desaparecen al cruzar el límite izquierdo de la pantalla
      if enemigo.x < (x_offset - enemigo.w):
        self.enemigos.remove(enemigo)

  def generar_enemigos(self, frames):
    # Los enemigos aparecen cada 3 segundos
    if (frames % (c.FPS * 3) == 0) and len(self.enemigos) < 4:
      enemigo = Enemigo(location=(c.UNIT * 20 + x_offset, c.UNIT * 4))
      self.enemigos.append(enemigo)
    
  def dibujar_enemigos(self):
    for enemigo in self.enemigos:
      enemigo.draw()


class Suelo(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=c.UV_SUELO)
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
    super().__init__(location, img_bank=0, uv=c.UV_BLOQUE_LADR)
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
    super().__init__(location, img_bank=0, uv=c.UV_TUBERIA, size=(c.UNIT * 2, c.UNIT * 2))
    self.tuberias = []
  
  # Método para colocar las tuberías
  def generar_tuberias(self):
    for location in c.TUBERIAS:
      tuberia = Tuberia(location)
      self.tuberias.append(tuberia)
  
  def dibujar_tuberias(self):
    for tuberia in self.tuberias:
      tuberia.draw()


class Arbusto(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=c.UV_ARBUSTO, size=(c.UNIT * 2, c.UNIT))
    self.arbustos = []
  
  # Método para colocar las tuberías
  def generar_arbustos(self):
    for location in c.ARBUSTOS:
      arbusto = Arbusto(location)
      self.arbustos.append(arbusto)
  
  def dibujar_arbustos(self):
    for arbusto in self.arbustos:
      arbusto.draw()


class Nube(Sprite):
  def __init__(self, location):
    super().__init__(location, img_bank=0, uv=c.UV_NUBE, size=(c.UNIT * 2, 23))
    self.nubes = []
  
  # Método para colocar las tuberías
  def generar_nubes(self):
    for location in c.NUBES:
      nube = Nube(location)
      self.nubes.append(nube)
  
  def dibujar_nubes(self):
    for nube in self.nubes:
      nube.draw()


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
    else:
      return False

  # Método llamado cuando Mario recoge una moneda
  def add_coin(self):
    self.coins += 1
