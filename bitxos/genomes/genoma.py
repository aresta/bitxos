import bitxos.consts
import random
import hashlib
import collections
import bitxos.neurons.networks as networks


Genes = collections.namedtuple('Genes', [
    'size',                 # in cms
    'weight',              # grams/cm. To calculate weight, linked to size
    'speed',
    'defense_units',
    'attack_units',
    'graze_units',          # pasturar
#    'aggressivity', # part of the genoma behaviour

    'organism_classification_neurons', 
    'quadrant_classification_neurons', 
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
#            random.randint(0, 100),     # aggressivity - 

            networks.get_random_neurons_array( 7, 8, 0),   # organism_classification_neurons -
            networks.get_random_neurons_array( 8*2, 4, 1),   # quadrant_classification_neurons -
            networks.get_random_neurons_array( 10+4, 4, 0),   # action_neurons -
        )
        new_genoma.hash = new_genoma.get_genes_hash()
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
            new_genes[gene_to_mutate] = _mutate_gene(new_genes[gene_to_mutate])
        else: 
            raise Exception("Wrong gene: [%s]" % new_genes[gene_to_mutate])

        new_genoma.genes = Genes(*new_genes)
        new_genoma.hash = new_genoma.get_genes_hash()
        return new_genoma

    def get_genes_hash(self):
        """Returns the hash of the genes"""
        assert self.genes, "Genoma has no genes. Can't calculate hash."
        return hashlib.sha256(str(self.genes).encode('utf-8')).hexdigest()

def _mutate_gene(gene):
    """Return a new gene as a identical tuple of tuples but with one of the values mutated"""
    layers_list = list(gene)
    layer_to_mutate = random.randrange(len(layers_list))
    layers_list[layer_to_mutate] = _mutate_layer( layers_list[layer_to_mutate])
    return tuple(layers_list)

def _mutate_layer(layer):
    groups = list(layer)  # weights and  biases
    group_to_mutate = random.randrange(1) # 0 or 1
    groups[group_to_mutate] = _mutate_group( groups[group_to_mutate])
    return tuple(groups)

def _mutate_group(group):
    group_list = list(group)
    elem_to_mutate = random.randrange(len(group_list))
    group_list[elem_to_mutate] = group_list[elem_to_mutate] * (random.choice([0.9,1.1])) # TODO: improve, extract const, check that is between 0 and 1
    return tuple(group_list)