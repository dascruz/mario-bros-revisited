""" Archivo para almacenar las constantes que usaremos en el juego
"""
# Medida para colocar los sprites
import random


UNIT = 16

# UV de los sprites
UV_MARIO = (80, 0)
UV_MARIO_SALTO = (96, 0)

UV_SUELO = (0, 16)
UV_TUBERIA = (48, 0)

UV_BLOQUE_OBJ = (0, 0)
UV_BLOQUE_LISO = (16, 0)
UV_BLOQUE_LADR = (32, 0)

UV_GOOMBA = (80, 16)
UV_GOOMBA_APLASTADO = (96, 16)
UV_KOOPA = (112, 0)
UV_CAPARAZON = (128, 0)

UV_ARBUSTO = (16, 16)
UV_NUBE = (0, 32)

UV_MONEDA = (144, 0)
UV_CHAMPI = (152, 0)
UV_FLOR = (168, 0)
UV_ESTRELLA = (184, 0)

# Tablero de juego
BOARD_WIDTH = 256
BOARD_HEIGHT = 256
BOARD_NAME = "Super Mario Bros (World 1-1)"
FPS = 60
TIME = 400

# Posición inicial de Mario
ALTURA_PERSONAJES = UNIT * 13
POS_MARIO = (UNIT * 3, ALTURA_PERSONAJES)

# Posición para los objetos que no deben ser visibles (objeto Bloque que contiene la lista de bloques, por ejemplo)
POS_DEFAULT = (-UNIT * 16, 0)

# Constantes para el movimiento de Mario
VELOCITY = 3
SPEED = 1.5
JUMP_HEIGHT = 4.5

# Constantes de los enemigos
ENEMY_SPEED = 1

# Ubicación del suelo
suelo_superior = [(i * UNIT, UNIT * 14) for i in range(UNIT * 5)]
suelo_inferior = [(i * UNIT, UNIT * 15) for i in range(UNIT * 5)]
SUELO = suelo_superior + suelo_inferior

# Ubicación manual de todos los bloques
ALTURA_BLOQUES = UNIT * 10
POS_BLOQUES = [17, 20, 21, 22, 23, 24, 30, 31, 32, 38, 41, 43]
BLOQUES = []
for pos in POS_BLOQUES:
  BLOQUES.append((UNIT * pos, ALTURA_BLOQUES))

# Ubicación manual de todas las tuberías
ALTURA_TUBERIAS = UNIT * 12
POS_TUBERIAS = [27, 35, 46]
TUBERIAS = []
for pos in POS_TUBERIAS:
  TUBERIAS.append((UNIT * pos, ALTURA_TUBERIAS))

# Ubicación de la decoración
POS_NUBES = [8, 18, 32, 33, 34, 44, 45]
NUBES = []
for pos in POS_NUBES:
  NUBES.append((UNIT * pos, UNIT * random.randint(4, 5)))

POS_ARBUSTOS = [11, 12, 13, 29, 33, 34]
ARBUSTOS = []
for pos in POS_ARBUSTOS:
  ARBUSTOS.append((UNIT * pos, ALTURA_PERSONAJES))