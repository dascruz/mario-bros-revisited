""" Archivo que contiene todos los objetos a usar en el videojuego
"""

import pyxel, random
import constantes as c

# Variable global utilizada para el movimiento de la cámara por el nivel
x_offset = 0


# Clase principal que heredan todos los objetos gráficos del juego
class Sprite:
  # Inicializamos la posición y cargamos el sprite correspondiente del banco de imágenes
  def __init__(self, uv: tuple, img_bank=0, location=c.POS_DEFAULT, size=(c.UNIT, c.UNIT), colkey=6):
    self.x = location[0]
    self.y = location[1]
    self.img_bank = img_bank
    self.u = uv[0]
    self.v = uv[1]
    self.w = size[0]
    self.h = size[1]
    self.colkey = colkey
  
  # Método para comprobar colisiones de un objeto con una lista de objetos
  # Devuelve el objeto con el que colisionamos
  def check_collision(self, objects):
    # Colisión tipo AABB. Source: https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
    for object in objects:
      if (self.x < object.x + object.w and self.x + self.w > object.x and
        self.y < object.y + object.h and self.h + self.y > object.y):
        return object
    
    return None

  # Método para dibujar en pantalla el sprite
  def draw(self):
    pyxel.blt(self.x - x_offset, self.y, self.img_bank, self.u, self.v,
              self.w, self.h, self.colkey)


# Clase auxiliar utilizada para generar objetos estáticos en el juego: bloques, suelo, nubes, arbustos y tuberías
class Generador():
  # Método para colocar los objetos del tipo tipo_objeto en las posiciones de la lista pos_objetos
  def generar_objetos(self, pos_objetos, tipo_objeto):
    objetos = []
    for posicion in pos_objetos:
      objeto = tipo_objeto(posicion)
      objetos.append(objeto)
    return objetos
  
  # Método para dibujar los objetos de la lista argumento
  def dibujar_objetos(self, objetos):
    for objeto in objetos:
      objeto.draw()


# Objeto encargado de las funciones de Mario
class Mario(Sprite):
  def __init__(self, location=c.POS_MARIO):
    super().__init__(location=location, img_bank=0, uv=(80, 0))
    # Empezamos con 3 vidas
    self.lives = 3

    # Variables utilizadas para el salto de Mario
    self.jump_time = c.JUMP_HEIGHT
    self.jump_active = False
  
  # Lógica para el movimiento de Mario, comprobando que no se sale de los límites de la pantalla
  def move(self):
    global x_offset

    # Movimiento horizontal con las teclas A y D
    if pyxel.btn(pyxel.KEY_D):
      if self.x > (c.UNIT * 5 + x_offset):
        x_offset += c.SPEED
      self.w = c.UNIT
      self.x = self.x + c.SPEED
    elif pyxel.btn(pyxel.KEY_A):
      self.w = -c.UNIT
      self.x = max(self.x - c.SPEED, 0 + x_offset)
    
    # Lógica para el salto de Mario, funciona como un movimiento parabólico en el eje Y
    if not (self.jump_active):
      if pyxel.btnp(pyxel.KEY_SPACE):
        self.jump_active = True
        self.u, self.v = c.UV_MARIO_SALTO
    else: 
      if self.jump_time >= -c.JUMP_HEIGHT:
        self.y -= (self.jump_time * abs(self.jump_time)) * 0.5
        self.jump_time -= 0.25
      else:
        self.jump_time = c.JUMP_HEIGHT
        self.jump_active = False
        self.u, self.v = c.UV_MARIO


class Enemigo(Sprite):
  def __init__(self, location=c.POS_DEFAULT):
    super().__init__(location=location, img_bank=0, uv=c.UV_GOOMBA)
    self.enemigos = []

    # Hay un 25% de probabilidades de que sea Koopa Troopa, y un 75% de que sea un Goomba
    prob = random.uniform(0, 1)
    if prob < 0.25:
      self.u, self.v = c.UV_KOOPA
      self.w = -c.UNIT
      self.h = 23
      self.tipo = "koopa"
    else:
      self.tipo = "goomba"
  
  # Lógica del movimiento de los enemigos
  def move(self):
    for enemigo in self.enemigos:
      enemigo.x -= c.ENEMY_SPEED

      # El enemigo aparece en el cielo para añadir variedad al movimiento (puede caer encima de un bloque por ejemplo)
      if enemigo.y + enemigo.h < c.UNIT * 14:
        enemigo.y += c.VELOCITY

      # Los enemigos mueren al cruzar el límite izquierdo de la pantalla
      if enemigo.x < x_offset - c.UNIT:
        self.enemigos.remove(enemigo)

  def generar_enemigos(self, frames):
    # Los enemigos aparecen cada 3-5 segundos, con un máximo de 4 enemigos simultáneamente
    if (frames % (c.FPS * random.randint(3, 5)) == 0) and len(self.enemigos) < 4:
      enemigo = Enemigo(location=(c.UNIT * 20 + x_offset, c.UNIT * 4))
      self.enemigos.append(enemigo)
    
  def dibujar_enemigos(self):
    for enemigo in self.enemigos:
      enemigo.draw()


class Suelo(Sprite):
  def __init__(self, location):
    super().__init__(location=location, uv=c.UV_SUELO)


class BloqueLadrillo(Sprite):
  def __init__(self, location):
    super().__init__(location=location, uv=c.UV_BLOQUE_LADR)


class BloqueObjeto(Sprite):
  def __init__(self, location):
    super().__init__(location=location, uv=c.UV_BLOQUE_OBJ)


class BloqueMoneda(Sprite):
  def __init__(self, location):
    super().__init__(location=location, uv=c.UV_BLOQUE_OBJ)


class Tuberia(Sprite):
  def __init__(self, location):
    super().__init__(location=location, uv=c.UV_TUBERIA, size=(c.UNIT * 2, c.UNIT * 2))


class Arbusto(Sprite):
  def __init__(self, location):
    super().__init__(location=location, uv=c.UV_ARBUSTO, size=(c.UNIT * 2, c.UNIT))


class Nube(Sprite):
  def __init__(self, location):
    super().__init__(location=location, uv=c.UV_NUBE, size=(c.UNIT * 2, 23))


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
    pyxel.blt(c.UNIT * 5.2, altura2 - 4, 0, c.UV_MONEDA[0], c.UV_MONEDA[1], 8, 14, 6)
    pyxel.text(c.UNIT * 6, altura2, "x " + f"{self.coins:02d}", 7)

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
