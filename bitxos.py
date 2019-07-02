import json
from bitxos.genomes.genoma import Genoma
from bitxos.organisms.organism import Organism
from bitxos.world.world import World

random_genoma = Genoma.getRandom()
print( random_genoma)
print( random_genoma.genes['size'])
print( random_genoma.genes['density'])

random_organism = Organism.getRandom()
print( random_organism)
print( random_organism.energy)
print( random_organism.weight)

#print( json.dumps(random_genoma.genes, sort_keys=True))
print( random_genoma.hash)

w = World()
for i in range(100): w.organisms.append( Organism.getRandom())

for o in w.organisms: print( o.genoma.hash )
