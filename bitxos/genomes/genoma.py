import bitxos.consts
import random
import json
import hashlib


class Genoma():
    def __init__(self):
        self.hash = None  # unique per each equivalent genoma

        self.genes = {
            'size': None,      # in cms
            'density': None,    # grams/cm. To calculate weight, linked to size
            'speed': None,
            'defense_units': None,
            'attack_units': None,
            'graze_units': None,   # pasturar
            'aggressivity': None,

            'vision_short_neurons': None,
            'vision_long_neurons': None,
            'action_neurons': None,
        }

    @classmethod
    def getRandom(cls):
        """ Returns a new created random genoma """
        new_genoma = Genoma()
        new_genoma.genes['size'] = random.randint(1, 200)  # 1cm to 2m 
        new_genoma.genes['density'] = random.randint(200, 500)  # organism of 100cm => from 20kg to 50kg 
        new_genoma.genes['speed'] = random.randint(1, 4)  # 1 to 4 cell per step 
        new_genoma.genes['defense_units'] = random.randint(0, 100)  # like grams of it,  for the energy cost
        new_genoma.genes['attack_units'] = random.randint(0, 100)  # 
        new_genoma.genes['graze_units'] = random.randint(0, 100)  # 
        new_genoma.genes['aggressivity'] = random.randint(0, 100)  # 

        new_genoma.genes['vision_short_neurons'] = None  # TODO
        new_genoma.genes['vision_long_neurons'] = None
        new_genoma.genes['action_neurons'] = None
        new_genoma.hash = hashlib.sha256( 
            json.dumps(new_genoma.genes, sort_keys=True)
            .encode('utf-8')).hexdigest()  # works only if all keys are strings TODO: check with neurons if it still works
        return new_genoma


