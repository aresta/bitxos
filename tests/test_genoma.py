import unittest
from bitxos.genomes.genoma import Genoma
from bitxos.genomes.genoma import _mutate_gene


class GenomaTestCase(unittest.TestCase):

    def test_genoma_random(self):
        random_genoma = Genoma.get_random()
        self._genoma_tests(random_genoma)
        
    def test_mutate_neurons(self):
        random_genoma = Genoma.get_random()
        new_gene = _mutate_gene(random_genoma.genes.organism_classification_neurons)
        self.assertNotEqual(new_gene, random_genoma.genes.organism_classification_neurons)

    def test_genoma_mutated(self):
        random_genoma = Genoma.get_random()
        mutated_genoma = random_genoma.get_mutated_copy()
        self._genoma_tests(mutated_genoma)
        self.assertNotEqual(random_genoma.hash, mutated_genoma.hash)

    def _genoma_tests(self, genoma):
        self.assertIsNotNone(genoma.hash)
        self.assertIsNotNone(genoma.genes)
        self.assertGreater(genoma.genes.size, 0)
        self.assertIsNotNone(genoma.genes.action_neurons)

    