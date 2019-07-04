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
        for i in range(20):
            w.organisms.append(last_organism)
            last_organism = last_organism.get_mutated_copy()
        o1, o2 = last_organism.get_quadrants_view()
        self.assertIsNotNone(o1)
        self.assertIsNotNone(o2)
