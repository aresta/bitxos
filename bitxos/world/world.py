import bitxos.consts
from bitxos.world.land import Land

class World:
    def __init__(self):
        self.time = 0
        self.land = Land()
        self.organisms = []
