""" Archivo que contiene todos los objetos a usar en el videojuego
"""

import pyxel, random
import constantes as c

# Variable global utilizada para el movimiento de la cámara por el nivel
x_offset = 0


# Clase principal que heredan todos los objetos gráficos del juego
class Sprite:
  # Inicializamos la posición y cargamos el sprite correspondiente del banco de imágenes
  def __init__(self, uv: tuple, img_bank=0, posicion=c.POS_DEFAULT, size=(c.UNIT, c.UNIT), colkey=6):
    self.x = posicion[0]
    self.y = posicion[1]
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
    top = self.y
    bottom = self.y + self.h
    left = self.x
    right = self.x + abs(self.w)
    for object in objects:
      obj_top = object.y
      obj_bottom = object.y + object.h
      obj_left = object.x
      obj_right = object.x + object.w
      if (left < obj_right and right > obj_left and top < obj_bottom and bottom > obj_top):
        # Colisión detectada. Ahora hay que ver por qué lado del objeto estamos colisionando utilizando la distancia mínima
        distancia = min(abs(left - obj_right), abs(right - obj_left), abs(top - obj_bottom), abs(bottom - obj_top))
        if distancia == abs(top - obj_bottom):
          return (object, "bottom")
        elif distancia == abs(bottom - obj_top):
          return (object, "top")
        elif distancia == abs(left - obj_right):
          return (object, "right")
        elif distancia == abs(right - obj_left):
          return (object, "left")
    
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
  def __init__(self, posicion=c.POS_MARIO):
    super().__init__(posicion=posicion, uv=(80, 0))
    # Empezamos con 3 vidas
    self.lives = 3

    # Variables utilizadas para el salto de Mario
    self.jump_time = 0
    self.jump_active = False
    self.grounded = False
  
  # Lógica para el movimiento de Mario, comprobando que no se sale de los límites de la pantalla
  def move(self, colisiones):
    global x_offset
    colision = self.check_collision(colisiones)
    if colision != None:
      obj_colision = colision[0]
      direccion = colision[1]

    # Movimiento horizontal con las teclas A y D
    if pyxel.btn(pyxel.KEY_D):
      self.w = c.UNIT
      if colision and direccion == "left":
        self.x = obj_colision.x - self.w
      else:
        if self.x > (c.UNIT * 5 + x_offset):
          x_offset += c.SPEED
        self.x += c.SPEED
    elif pyxel.btn(pyxel.KEY_A):
      self.w = -c.UNIT
      if colision and direccion == "right":
        self.x = obj_colision.x + obj_colision.w
      else:
        self.x = max(self.x - c.SPEED, 0 + x_offset)
    
    if (colision and direccion == "top") or self.y >= c.ALTURA_PERSONAJES:
      if colision and isinstance(obj_colision, Enemigo):
        if obj_colision.tipo == "goomba":
          obj_colision.u, obj_colision.v = c.UV_GOOMBA_APLASTADO
      self.grounded = True
    else:
      self.grounded = False   
    
    # Si Mario está pisando tierra, podemos saltar
    if self.grounded:
      if colision:
        self.y = obj_colision.y - self.h
      else:
        self.y = c.ALTURA_PERSONAJES
      self.u, self.v = c.UV_MARIO
      self.jump_time = -0.1

      if pyxel.btn(pyxel.KEY_SPACE):
        self.jump_time = c.JUMP_HEIGHT
        self.u, self.v = c.UV_MARIO_SALTO
        self.y -= 0.1
        self.grounded = False
    else:
      self.y = self.y - self.jump_time
      self.jump_time -= 0.1
      self.jump_time = self.jump_time

      # Si Mario golpea con la cabeza un bloque de objeto, este se convierte en uno liso
      if colision and direccion == "bottom":
        self.y = obj_colision.y + obj_colision.h
        self.jump_time = -2
        if isinstance(obj_colision, BloqueObjeto):
          obj_colision.u, obj_colision.v = c.UV_BLOQUE_LISO


# Objeto encargado de la generación de enemigos
class Enemigo(Sprite):
  def __init__(self, posicion=c.POS_DEFAULT):
    super().__init__(posicion=posicion, uv=c.UV_GOOMBA)
    self.enemigos = []
    # True indica movimiento hacia la izquierda, False hacia la derecha
    self.direccion = True

    # Hay un 25% de probabilidades de que sea Koopa Troopa, y un 75% de que sea un Goomba
    prob = random.uniform(0, 1)
    if prob < 0.25:
      self.u, self.v = c.UV_KOOPA
      self.w = -c.UNIT
      # El Koopa Troopa es más alto
      self.h = 23
      self.tipo = "koopa"
    else:
      self.tipo = "goomba"
  
  # Lógica del movimiento de los enemigos
  def move(self, colisiones):
    for enemigo in self.enemigos:
      # Comprobamos colisiones
      colision = enemigo.check_collision(colisiones)
      if colision != None:
        obj_colision = colision[0]
        direccion = colision[1]

      # Cambia de dirección si se choca con un objeto
      if colision and (direccion == "left" or direccion == "right"):
        enemigo.direccion = not enemigo.direccion
        if enemigo.tipo == "koopa":
          enemigo.w = -enemigo.w

      # Movimiento del enemigo
      if enemigo.direccion:
        enemigo.x -= c.ENEMY_SPEED
      else:
        enemigo.x += c.ENEMY_SPEED

      if enemigo.y + enemigo.h < c.ALTURA_PERSONAJES + c.UNIT:
        enemigo.y += c.VELOCITY

      # Los enemigos mueren al cruzar el límite izquierdo de la pantalla
      if enemigo.x < x_offset - c.UNIT:
        self.enemigos.remove(enemigo)

  def generar_enemigos(self, frames):
    # Los enemigos aparecen cada 3-5 segundos, con un máximo de 4 enemigos simultáneamente
    # El enemigo aparece en el cielo para añadir variedad al movimiento (puede caer encima de un bloque por ejemplo)
    if (frames % (c.FPS * random.randint(3, 5)) == 0) and len(self.enemigos) < 4:
      enemigo = Enemigo(posicion=(c.UNIT * 20 + x_offset, c.UNIT * 3))
      self.enemigos.append(enemigo)
    return self.enemigos
    
  def dibujar_enemigos(self):
    for enemigo in self.enemigos:
      enemigo.draw()


# Objetos estáticos y decorativos

class Suelo(Sprite):
  def __init__(self, posicion):
    super().__init__(posicion=posicion, uv=c.UV_SUELO)


class BloqueLadrillo(Sprite):
  def __init__(self, posicion):
    super().__init__(posicion=posicion, uv=c.UV_BLOQUE_LADR)


class BloqueObjeto(Sprite):
  def __init__(self, posicion):
    super().__init__(posicion=posicion, uv=c.UV_BLOQUE_OBJ)


class BloqueMoneda(Sprite):
  def __init__(self, posicion):
    super().__init__(posicion=posicion, uv=c.UV_BLOQUE_OBJ)


class Tuberia(Sprite):
  def __init__(self, posicion):
    super().__init__(posicion=posicion, uv=c.UV_TUBERIA, size=(c.UNIT * 2, c.UNIT * 2))


class Arbusto(Sprite):
  def __init__(self, posicion):
    super().__init__(posicion=posicion, uv=c.UV_ARBUSTO, size=(c.UNIT * 2, c.UNIT))


class Nube(Sprite):
  def __init__(self, posicion):
    super().__init__(posicion=posicion, uv=c.UV_NUBE, size=(c.UNIT * 2, 23))


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
  def check_time(self, frames):
    # Un segundo equivale a 60 fotogramas
    if frames % c.FPS == 0:
      self.time -= 1

    if self.time < 0:
      self.time = c.TIME
      return True
    else:
      return False

  # # Método llamado cuando Mario recoge una moneda
  # def add_coin(self):
  #   self.coins += 1
