import unittest
from bitxos.genomes.genoma import Genoma
from bitxos.organisms.organism import Organism
from bitxos.world.world import World


class OrganismTestCase(unittest.TestCase):

    def test_organism(self):
        random_organism = Organism.get_random()
        self.assertIsNotNone(random_organism.genoma)
        self.assertIsNotNone(random_organism.genoma.hash)
        self.assertIsNotNone(random_organism.energy)
        
        clone = random_organism.get_clone()
        self.assertEqual(random_organism.genoma.hash, clone.genoma.hash, "Clone has different hash")
        
        mutated = random_organism.get_mutated_copy()
        self.assertNotEqual(random_organism.genoma.hash, mutated.genoma.hash, "Mutated has same hash")

    def test_distance(self):
        org1 = Organism.get_random()
        org2 = Organism.get_random()
        self.assertGreaterEqual(org1.distance(org2), 0)

    def test_quadrants(self):
        w = World.getWorld()
        last_organism = Organism.get_random()
        for _ in range(40):
            w.organisms.append(last_organism)
            last_organism = last_organism.get_random()
        o1, o2 = last_organism.get_quadrants_view()
        print("quads", o1,o2)
        self.assertIsNotNone(o1)
        self.assertIsNotNone(o2)

    def test_actions(self):
        w = World.getWorld()
        last_organism = Organism.get_random()
        for _ in range(500):
            w.organisms.append(last_organism)
            last_organism = last_organism.get_random()
        acts, st = last_organism.get_actions()
        self.assertIsNotNone(acts)
        self.assertIsNotNone(st)

