import unittest
from bitxos.genomes.genoma import Genoma
from bitxos.organisms.organism import Organism


class GenomaTestCase(unittest.TestCase):

    def test_genoma(self):
        random_genoma = Genoma.getRandom()
        self.assertGreater(random_genoma.genes['size'], 0)

    def test_organism(self):
        random_organism = Organism.getRandom()
        self.assertEqual(random_organism.size * random_organism.genoma.genes['density'], random_organism.weight)
