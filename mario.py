import pyxel, random
from . import clases
from . import constantes


class App:
    def __init__(self):
        # Resolución de la NES (256 x 240)
        pyxel.init(256, 240, caption="Super Mario Bros (World 1-1)")
        pyxel.load("assets/mario.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass


App()
