import collections
import numpy as np
import bitxos.neurons.networks as networks

def _organism_classify(organism, network):
    """Neural network to classify an organism out of its visible attributes"""
    res = 0
    inputs = np.array([[
        organism.genoma.genes.size,
        organism.genoma.genes.weight,
        organism.genoma.genes.speed,
        organism.genoma.genes.defense_units,
        organism.genoma.genes.attack_units,
        organism.genoma.genes.graze_units,        
        organism.age
        ]])
    network = networks._get_general_network(7,3,0)
    networks._set_weights(network, organism.genoma.genes.organism_classification_neurons)
    # print("organism_classification_neurons", organism.genoma.genes.organism_classification_neurons)
    res = networks._predict(network, inputs)
    return res 


def quadrant_analysis(quadrant, network):
    """Neural network to analyze a quadrant in the view field of the organism based in the elements seen in it"""
    # print("quadrant 1", quadrant)
    quadrant = [_organism_classify(o, network) for o in quadrant]
    # print("quadrant 2", quadrant)
    quadrant = collections.Counter(quadrant)  # counts how many of each type we have
    quadrant = [quadrant[n] if n in quadrant else 0 for n in range(16)]
    #  TODO: pass NN

    return quadrant


