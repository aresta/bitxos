import bitxos.consts
import random


class Genoma():
    def __init__(self):
        self.id = None  # TODO: generate ID, or in another init method...
        self.size = None      # in cms
        self.density = None    # grams/cm. To calculate weight, linked to size
        self.speed = None
        self.defense_units = None
        self.attack_units = None
        self.graze_units = None   # pasturar
        self.aggressivity = None

        self.vision_short_neurons = None
        self.vision_long_neurons = None
        self.action_neurons = None

    @classmethod
    def getRandom(cls):
        """ Returns a new created random genoma """
        new_genoma = Genoma()
        new_genoma.size = random.randint(1, 200)  # 1cm to 2m 
        new_genoma.density = random.randint(200, 500)  # organism of 100cm => from 20kg to 50kg 
        new_genoma.speed = random.randint(1, 4)  # 1 to 4 cell per step 
        new_genoma.defense_units = random.randint(0, 100)  # like grams of it,  for the energy cost
        new_genoma.attack_units = random.randint(0, 100)  # 
        new_genoma.graze_units = random.randint(0, 100)  # 
        new_genoma.aggressivity = random.randint(0, 100)  # 

        new_genoma.vision_short_neurons = None  # TODO
        new_genoma.vision_long_neurons = None
        new_genoma.action_neurons = None
        return new_genoma

