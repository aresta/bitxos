import bitxos.consts
import random
import json
import hashlib
import collections


Genes = collections.namedtuple('Genes', [
    'size',                 # in cms
    'weight',              # grams/cm. To calculate weight, linked to size
    'speed',
    'defense_units',
    'attack_units',
    'graze_units',          # pasturar
    'aggressivity', 

    'organism_classification_neurons', 
    'vision_short_neurons', 
    'vision_long_neurons', 
    'action_neurons', 
])


class Genoma():
    def __init__(self):
        self.hash = None  # unique per each equivalent genoma
        self.genes = None  # defined above

    @classmethod
    def get_random(cls):
        """Returns a new created random genoma"""
        new_genoma = Genoma()
        size = random.randint(1, 200)
        new_genoma.genes = Genes(
            size,                       # size in cm - 1cm to 2m  
            size * random.randint(200, 500),   # weight in gr - organism of 100cm => from 20kg to 50kg  
            random.randint(1, 4),       # speed - 1 to 4 cell per step  
            random.randint(0, 100),     # defense_units - like grams of it for the energy cost 
            random.randint(0, 100),     # attack_units - 
            random.randint(0, 100),     # graze_units - 
            random.randint(0, 100),     # aggressivity - 

            ((1, 0, 1), (1, 0, 1)),   # TODO vision_short_neurons -
            ((1, 0, 1), (1, 0, 1)),   # vision_long_neurons -
            ((1, 0, 1), (1, 0, 1)),   # vision_long_neurons -
            ((1, 0, 1), (1, 0, 1)),   # action_neurons -
        )
        new_genoma.hash = new_genoma._get_genes_hash()
        return new_genoma

    def get_mutated_copy(self, rate=1):
        """Returns a new created genoma with same genes but mutated.

            rate -- 1: basic small change, 2:bigger, etc 
        """
        new_genoma = Genoma()
        new_genes = list(self.genes)

        gene_to_mutate = random.randrange(len(new_genes))
        if isinstance(new_genes[gene_to_mutate], int):     # TODO: mutate also the neurons
            amount = abs(new_genes[gene_to_mutate]) * rate / 100  # for rate = 1 will change +- 1%
            amount = max(round(amount), 1)  # at least we change in 1 TODO: check this, smaller gens will get more relative impact
            new_genes[gene_to_mutate] += random.choice([amount, -amount])
        elif isinstance(new_genes[gene_to_mutate], tuple):
            new_genes[gene_to_mutate] = self._mutate_neurons(new_genes[gene_to_mutate])
        else: 
            raise Exception("Wrong gene: [%s]" % new_genes[gene_to_mutate])

        new_genoma.genes = Genes(*new_genes)
        new_genoma.hash = new_genoma._get_genes_hash()
        return new_genoma

    def _get_genes_hash(self):
        """Returns the hash of the genes"""
        assert self.genes, "Genoma has no genes. Can't calculate hash."
        return hashlib.sha256(str(self.genes).encode('utf-8')).hexdigest()  # TODO: check with neurons if it still works

    def _mutate_neurons(self, neurons):
        neurons_list = list(neurons)    
        neurons_list = [list(n) for n in neurons_list]  # convert tuple of tuples in list of lists

        layer_to_mutate = random.randrange(len(neurons_list))
        layer = neurons_list[layer_to_mutate]
        gen_to_mutate = random.randrange(len(layer))
        layer[gen_to_mutate] += random.choice([-1, 1])  # TODO: check how to mutate it

        neurons_list = [tuple(n) for n in neurons_list]  # convert back to tuple of tuples
        return tuple(neurons_list)
