from bitxos.genomes.genoma import Genoma
from bitxos.organisms.organism import Organism

random_genoma = Genoma.getRandom()
print( random_genoma)
print( random_genoma.size)
print( random_genoma.density)

random_organism = Organism.getRandom()
print( random_organism)
print( random_organism.energy)
print( random_organism.weight)