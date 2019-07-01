import bitxos.consts


class World:
    def __init__(self):
        self.time = 0
        self.land = Land()
        self.genomes = {}
        self.organisms = []
