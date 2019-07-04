import random
import math
import collections
import bitxos.consts as consts
import bitxos.neurons.vision as vision
from bitxos.genomes.genoma import Genoma
from bitxos.world.world import World


class Organism:
    def __init__(self):
        self.genoma = None
        self.energy = None
        self.damage = 0

        self.x = 0
        self.y = 0

        self.born_at = None
        self.last_fight_at = None
        self.state_record = []

    @property
    def size(self):
        """returns the size in cms"""
        return self.genoma.genes.size

    @property
    def weight(self):
        """returns the weight in grams"""
        return self.genoma.genes.weight

    def __repr__(self):
        return "<x=%s y=%s>" % (self.x, self.y)

    @classmethod
    def get_random(cls):
        """Returns a new created random organism with a new created random genoma"""
        new_organism = Organism()
        new_organism.genoma = Genoma.get_random()  # TODO: posa'l a l'array i guarda ID
        new_organism.energy = new_organism.weight // random.randint(3, 4)
        new_organism.x = random.randint(0, consts.WORLD_WIDTH)
        new_organism.y = random.randint(0, consts.WORLD_HEIGHT)
        new_organism.born_at = World.time
        return new_organism

    def get_clone(self):
        """Returns a new created organism with same exact genoma"""
        new_organism = self._create_new_organism_body()
        new_organism.genoma = self.genoma  # we can do this because genoma is inmutable
        return new_organism

    def get_mutated_copy(self, rate=1):
        """Returns a new created organism with same genoma but mutated.

            rate -- 1: basic small change, 2:bigger, etc 
        """
        new_organism = self._create_new_organism_body()
        new_organism.genoma = self.genoma.get_mutated_copy()
        return new_organism

    def _create_new_organism_body(self):
        """Returns a new created organism without genoma but with energy and so on based in self"""
        new_organism = Organism()
        new_organism.energy = self.energy // 4  # TODO: calculate better the energy to give
        self.energy -= new_organism.energy
        new_organism.x = self.x + random.randint(-10, 10)  # TODO: think about this 
        new_organism.y = self.y + random.randint(-10, 10)  # TODO: think about this
        new_organism.born_at = World.time
        return new_organism

    def distance(self, organism):
        """Returns the distance to the organism"""
        return round(math.hypot(self.x - organism.x, self.y - organism.y))

    def get_quadrants_view(self):
        """Returns 16 quadrants: 8 near + 8 far areas, each with a tuple of its elements"""
        world = World.getWorld()
        orgs_near, orgs_far = world.get_organism_at_distances(self, 20, 200)

        organism_in_quadrants_near = self._classify_in_quadrants(orgs_near)
        organism_in_quadrants_far = self._classify_in_quadrants(orgs_far)
        quadrants_near = [vision.quadrant_analysis(q, None) for q in organism_in_quadrants_near]
        quadrants_far = [vision.quadrant_analysis(q, None) for q in organism_in_quadrants_far]
        print(quadrants_near)

        return quadrants_near, quadrants_far

    def get_action(self, quadrants_near, quadrants_far):
        """Returns the next action to do based in the situation in the quadrants around and in the current internal state.
           Returns also the new state.
        """
        return
        
    def _classify_in_quadrants(self, orgs):
        q_N, q_NE, q_E, q_SE, q_S, q_SW, q_NW, q_W = [], [], [], [], [], [], [], []
        for o in orgs:
            if o.y >= self.y:
                if o.x >= self.x:
                    if (o.y - self.y) >= (o.x - self.x):
                        q_N.append(o)
                    else:
                        q_NE.append(o)
                else:
                    if (o.y - self.y) >= (self.x - o.x):
                        q_NW.append(o)
                    else:
                        q_W.append(o)
            else:
                if o.x >= self.x:
                    if (o.y - self.y) >= (o.x - self.x):
                        q_E.append(o)
                    else:
                        q_SE.append(o)
                else:
                    if (o.y - self.y) >= (self.x - o.x):
                        q_SW.append(o)
                    else:
                        q_S.append(o)
        return q_N, q_NE, q_E, q_SE, q_S, q_SW, q_NW, q_W
