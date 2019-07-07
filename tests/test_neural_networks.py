import unittest
import numpy as np
import keras
import bitxos.neurons.networks as networks


class NNTestCase(unittest.TestCase):

    def test_multiclassification(self):
        model = networks._get_multiclassification_network(8, 3, 1)  # 8 inputs, 3 outputs, 1 hidden layer
        l_1 = np.reshape(range(9 * 8), (9, 8))  # hidden layer: weights: 8 inputs + 1 biases, 8 outpus
        l_2 = np.reshape(range(9 * 3), (9, 3))  # output layer: weights: 8 inputs + 1 biases, 3 outpus

        # networks._set_weights(model, [l_1,l_2])
        networks._set_weights(model, networks.get_random_neurons_array(8,3,1))
        inputs = np.array([range(8)])
        res = networks._predict(model, inputs)
        self.assertIn(res, (0,1,2))

    def test_get_random_neurons(self):
        neurons = networks.get_random_neurons_array(8,4,1)
        self.assertEqual( len(neurons), 2)
        self.assertEqual( len(neurons[0]), 9)
        layer = neurons[0]

        self.assertIsInstance(layer, tuple)
        weights = layer[0]
        self.assertIsInstance(weights, tuple)
        self.assertIsInstance(weights[0], float)
        biases = layer[1]
        self.assertIsInstance(biases, tuple)
        self.assertIsInstance(biases[0], float)

    