import random
import bitxos.consts as consts
from bitxos.genomes.genoma import Genoma


class Organism:
    def __init__(self):
        self.genoma = None
        self.energy = None
        self.damage = 0

        self.x = 0
        self.y = 0

        self.born_at = None
        self.last_fight_at = None
        self.state_record = []

    @property
    def size(self):
        """ returns the size in cms """
        return self.genoma.genes['size']

    @property
    def weight(self):
        """ returns the weight in grams """
        return self.genoma.genes['size'] * self.genoma.genes['density']

    @classmethod
    def getRandom(cls):
        """ Returns a new created random organism with a new created random genoma """
        new_organism = Organism()
        new_organism.genoma = Genoma.getRandom()  # TODO: posa'l a l'array i guarda ID
        new_organism.energy = new_organism.weight / random.randint(2, 4)
        new_organism.x = random.randint(0, consts.WORLD_WIDTH)
        new_organism.y = random.randint(0, consts.WORLD_HEIGHT)
        return new_organism
