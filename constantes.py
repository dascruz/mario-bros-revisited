""" Archivo para almacenar las constantes que usaremos en el juego
"""
# Medida para colocar los sprites
UNIT = 16

# Tablero de juego
BOARD_WIDTH = 256
BOARD_HEIGHT = 256
BOARD_NAME = "Super Mario Bros (World 1-1)"
FPS = 60
TIME = 400

# Posición inicial de Mario
POS_MARIO = (UNIT * 3, UNIT * 13)

# Constantes para el movimiento de Mario
VELOCITY = 3
SPEED = 1.5
JUMP_HEIGHT = 4.5

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
ALTURA_TUBERIAS = UNIT * 13
POS_TUBERIAS = [27, 35, 46]
TUBERIAS = []
for pos in POS_TUBERIAS:
  TUBERIAS.append((UNIT * pos, ALTURA_TUBERIAS))