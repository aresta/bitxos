import random
import pyglet
from bitxos.genomes.genoma import Genoma
from bitxos.organisms.organism import Organism
from bitxos.world.world import World
import pprint

window = pyglet.window.Window(1000, 1000)
batch = pyglet.graphics.Batch()
vertex = []
blau = (0, 0, 255)
vermell = (255, 0, 0)

world = World.getWorld()

for _ in range(10):
    world.organisms.append( Organism.get_random() )

pp = pprint.PrettyPrinter(indent=4)
for n in range(5):
    to_add = []
    for org in world.organisms:
        print("org", org)
        # pp.pprint( org.genoma.genes.organism_classification_neurons )     
        # pp.pprint( org.get_mutated_copy().genoma.genes.organism_classification_neurons )     
        print(org.get_actions())
        print(". . . . . . . . . . .")
        i = random.randint(0, len(world.organisms)-1)
        to_add.append( world.organisms[i].get_mutated_copy())
    world.organisms.extend( to_add)
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-", n)
    

v1 = []
c = []
for organism in world.organisms:
    v1.append(organism.x)
    v1.append(organism.y)
    c.append(random.randint(20, 255))
    c.append(random.randint(20, 255))
    c.append(random.randint(20, 255))
num = int(len(v1) / 2)
v2 = batch.add(num, pyglet.gl.GL_POINTS, None,
    ('v2i/stream', v1),
    ('c3B/stream', c))


def update(dt):
    # batch = pyglet.graphics.Batch()
    for b in vertex:
        d = random.randint(-5, 5)
        b.vertices = [v + d for v in b.vertices]


pyglet.clock.schedule_interval(update, 1 / 4)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    print(symbol)
    pass


pyglet.app.run()

