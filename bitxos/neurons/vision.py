import collections


def _organism_classify(organism, network):
    """Neural network to classify an organism out of its visible attributes"""
    res = 0
    #  TODO: pass NN
    if organism.genoma.genes.size > 100:
        res += 1
    if organism.genoma.genes.weight > 10000:
        res += 2
    if organism.genoma.genes.defense_units > 50:
        res += 4
    if organism.genoma.genes.attack_units > 50:
        res += 8
    return res 


def quadrant_analysis(quadrant, network):
    """Neural network to analyze a quadrant in the view field of the organism based in the elements seen in it"""
    quadrant = [_organism_classify(o, network) for o in quadrant]
    quadrant = collections.Counter(quadrant)  # counts how many of each type we have
    quadrant = [quadrant[n] if n in quadrant else 0 for n in range(16)]
    #  TODO: pass NN

    return quadrant


# def view_analysis(quadrant, network):  # TODO: move to actions?
#     """Neural network to analyze all quadrants around the organism"""
#     pass