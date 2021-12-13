""" Archivo para almacenar las constantes que usaremos en el juego
"""

import random

# Medida para colocar los sprites
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
POS_MARIO = (UNIT * 3, ALTURA_PERSONAJES - UNIT * 1)

# Posición para los objetos que no deben ser visibles (objeto Bloque que contiene la lista de bloques, por ejemplo)
POS_DEFAULT = (-UNIT * 16, 0)

# Constantes para el movimiento de Mario
VELOCITY = 3
SPEED = 1.5
JUMP_HEIGHT = 3.8
FALL_SPEED = 0.2

# Constantes de los enemigos
ENEMY_SPEED = 0.8

# Ubicación del suelo
suelo_superior = [(i * UNIT, UNIT * 14) for i in range(UNIT * 16)]
suelo_inferior = [(i * UNIT, UNIT * 15) for i in range(UNIT * 16)]
SUELO = suelo_superior + suelo_inferior

# Ubicación manual de todos los bloques
ALTURA_BLOQUES = UNIT * 10
POS_BLOQUES_LADRILLO = [17, 20, 22, 24, 30, 31, 32, 38, 42, 43, 54, 56, 57, 60, 61, 62, 70, 72, 74]
BLOQUES_LADRILLO = []
for pos in POS_BLOQUES_LADRILLO:
  BLOQUES_LADRILLO.append((UNIT * pos, ALTURA_BLOQUES))

POS_BLOQUES_OBJETO = [23, 55, 71]
BLOQUES_OBJETO = [(UNIT * 22, UNIT * 7)]
for pos in POS_BLOQUES_OBJETO:
  BLOQUES_OBJETO.append((UNIT * pos, ALTURA_BLOQUES))

POS_BLOQUES_MONEDA = [21, 73]
BLOQUES_MONEDA = []
for pos in POS_BLOQUES_MONEDA:
  BLOQUES_MONEDA.append((UNIT * pos, ALTURA_BLOQUES))

# Ubicación manual de todas las tuberías
ALTURA_TUBERIAS = UNIT * 12
POS_TUBERIAS = [27, 35, 46, 65, 80, 100, 120, 132]
TUBERIAS = []
for pos in POS_TUBERIAS:
  TUBERIAS.append((UNIT * pos, ALTURA_TUBERIAS))

# Ubicación de la decoración
POS_NUBES = [8, 18, 32, 33, 34, 44, 45, 60, 63, 65, 68, 77, 83, 84, 88, 94, 95, 96, 100, 112, 113, 119, 123, 128]
NUBES = []
for pos in POS_NUBES:
  NUBES.append((UNIT * pos, UNIT * random.randint(4, 5)))

POS_ARBUSTOS = [11, 12, 13, 29, 33, 34, 38, 42, 43, 46, 47, 48, 56, 57, 63, 64, 76, 80, 90, 91, 92, 103, 108, 109, 116, 120, 126, 127]
ARBUSTOS = []
for pos in POS_ARBUSTOS:
  ARBUSTOS.append((UNIT * pos, ALTURA_PERSONAJES))
