import random
import pyglet
from bitxos.genomes.genoma import Genoma
from bitxos.organisms.organism import Organism
from bitxos.world.world import World


window = pyglet.window.Window(1000, 1000)
batch = pyglet.graphics.Batch()
vertex = []
blau = (0, 0, 255)
vermell = (255, 0, 0)

w = World.getWorld()
last_organism = Organism.get_random()

for i in range(500):
    w.organisms.append(last_organism)
    last_organism = last_organism.get_clone()

v1 = []
c = []
for o in w.organisms:
    v1.append(o.x)
    v1.append(o.y)
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

