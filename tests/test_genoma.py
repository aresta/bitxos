import unittest
from bitxos.genomes.genoma import Genoma
from bitxos.organisms.organism import Organism


class GenomaTestCase(unittest.TestCase):

    def test_genoma(self):
        random_genoma = Genoma.get_random()
        self._genoma_tests(random_genoma)
        mutated_genoma = random_genoma.get_mutated_copy()
        self._genoma_tests(mutated_genoma)
        self.assertNotEqual(random_genoma.hash, mutated_genoma.hash)
        self.assertAlmostEqual

    def _genoma_tests(self, genoma):
        self.assertIsNotNone(genoma.hash)
        self.assertIsNotNone(genoma.genes)
        self.assertGreater(genoma.genes.size, 0)
        self.assertIsNotNone(genoma.genes.action_neurons)

    