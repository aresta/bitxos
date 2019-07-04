import json
from bitxos.genomes.genoma import Genoma
from bitxos.organisms.organism import Organism
from bitxos.world.world import World

random_organism = Organism.get_random()
print("random_organism", random_organism)

w = World.getWorld()
last_organism = random_organism
for i in range(20000):
    w.organisms.append( last_organism)
    last_organism = Organism.get_random()

# for o in w.organisms:
#     print(o) 
    # print( "size",o.size )
    # print( "weight",o.weight )
    # print( "energy",o.energy )
    # print( "born_at",o.born_at )
    # print( "x",o.x )
    # print( "y",o.y )
    # print( o.genoma.genes )
    # print('++++++++++++++++++++++++++++')

n, f = random_organism.get_quadrants_view()
# print(n)
# print(f)
