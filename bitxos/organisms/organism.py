import random
import math
import bitxos.consts as consts
import bitxos.neurons.vision as vision
import bitxos.neurons.action as action
from bitxos.genomes.genoma import Genoma
from bitxos.world.world import World
import bitxos.neurons.networks as networks
import pprint
import numpy as np


class Organism:
    def __init__(self):
        self.genoma = None
        self.x = 0
        self.y = 0
        self.energy = None
        self.damage = 0
        self.age = 0
        self.last_fight_at = 0
        self.memory = []

    @property
    def size(self):
        """returns the size in cms"""
        return self.genoma.genes.size

    @property
    def weight(self):
        """returns the weight in grams"""
        return self.genoma.genes.weight

    @property
    def state(self):
        """returns the internal state of the organism at this moment in its life, except memory"""
        return (self.energy, self.damage, self.age, self.last_fight_at)

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
        new_organism.age = 0
        new_organism.last_fight_at = 0
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
        new_organism.x = self.x + random.randint(-10, 10)  # TODO: improve 
        new_organism.y = self.y + random.randint(-10, 10)  # TODO: improve
        new_organism.age = 0
        return new_organism

    def distance(self, organism):
        """Returns the distance to the organism"""
        return round(math.hypot(self.x - organism.x, self.y - organism.y))

    def angle(self, organism):
        """Returns the relative angle to the organism in radians"""
        return round(math.atan2(self.x - organism.x, self.y - organism.y))

    def get_quadrants_view(self):
        """Returns N quadrants with organisms"""
        world = World.getWorld()
        orgs = world.get_organism_at_distance(self, 200)
        quadrants = self._classify_in_quadrants( orgs ) # list of quadrants with list of organism objects
        
        network_organism_classification = networks._get_general_network( 7, 8, 0)  #TODO: number of org types, move to consts
        networks._set_weights( network_organism_classification, self.genoma.genes.organism_classification_neurons) 
        
        network_quadrant_classification = networks._get_general_network( 8*2, 4, 1) #TODO: number of quadrant types, move to consts
        networks._set_weights( network_quadrant_classification, self.genoma.genes.quadrant_classification_neurons)

        # pp = pprint.PrettyPrinter(indent=4)
        # print("quadrants")
        # pp.pprint(quadrants)
        quadrants_classified = []
        for n in range(10): #TODO: change by const
            quad = dict()
            if n in quadrants.keys():
                for (org, dist) in quadrants[n]:  # convert tuple (org,dist) to dict {org_type: [list of dists]}
                    org_type = vision.organism_classify( org, network_organism_classification)
                    if org_type in quad.keys():
                        quad[org_type].append(dist)
                    else:
                        quad[org_type] = [dist]
            else:
                quad = None #TODO: create a dict with all org types to empty. There is nobody there.

            # print("quadrants[quadrant]", quadrants[quadrant])
            # print("quad", quad)
            if quad:
                quad_res = vision.quadrant_classify( quad, network_quadrant_classification) # quadrant type value calculated by the network 
            else:
                quad_res = 0
            # print("quad_res", quad_res)
            quadrants_classified.append( quad_res )

        # print("quadrants", quadrants.keys())
        # print("quadrants_classified", quadrants_classified)
        return quadrants_classified

    def get_actions(self):
        """Returns the next action to do based in the situation in the quadrants around and in the current internal state.
           Returns also the new state.
        """
        quadrants = self.get_quadrants_view()

        network_actions = networks._get_general_network( 10+4, 4, 0) #TODO: number of quadrant types, move to consts
        networks._set_weights( network_actions, self.genoma.genes.action_neurons)

        actions, new_state = action.get_actions( quadrants, self.state, self.memory, network_actions)
        return actions, new_state

    def _classify_in_quadrants(self, orgs):
        num_quadrants = 10 # TODO: global or genoma var (?)
        
        quadrant_angle = math.pi * 2 / num_quadrants
        quadrants = dict()
        for org in orgs:  # TODO: improve...
            angle = self.angle( org[0] ) + math.pi # organism is the 1st element in the tuple. The second is distance.
            quadrant = math.floor(angle / quadrant_angle)
            if quadrant in quadrants.keys():
                quadrants[quadrant].append( org )
            else:
                quadrants[quadrant]= [ org ]
        #print("_classify_in_quadrants: ", quadrants)
        return quadrants
