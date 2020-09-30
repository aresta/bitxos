import collections
import numpy as np
import bitxos.neurons.networks as networks

def organism_classify(organism, network):
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
    res = networks._predict( network, inputs)
    # print("organism_classify inputs:", inputs, "res", res)
    return res 


def quadrant_classify(quadrant, network):
    """Neural network to analyze a quadrant in the view field of the organism based in the org_types and distances to each seen in it"""
    
    quadrant_orgs_distances = [] 
    for n in range(8):
        if n in quadrant.keys():
            dists = quadrant[n] # distances of all orgs of this type in this quadrant
            quadrant_orgs_distances.extend([ len(dists), sum(dists)/len(dists)]) # for in n (org type) we add the number of this orgs in the quadrant, and the average of distances
        else:
            quadrant_orgs_distances.extend([ 0, 0])

    # print("quadrant_orgs_distances", quadrant_orgs_distances)
    
    res = networks._predict(network, np.array([quadrant_orgs_distances]))
    return res 


