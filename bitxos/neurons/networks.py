import numpy as np
import keras
import random
from keras.models import Sequential
from keras.layers import Dense


def _get_multiclassification_network(inputs_len, outputs_len, hidden_layers):
    """Returns a multiclass classification neural network.        
        Only one output should be right e.g. direction to move. Sum of all outputs is 1"""
    return _get_neural_network(inputs_len, outputs_len, hidden_layers, 'softmax')

def _get_general_network(inputs_len, outputs_len, hidden_layers):
    """Returns a 'sigmoid' neural network.        
        Several outputs can be true e.g.  types of organisms seen around. Sum of all outputs is not 1"""
    return _get_neural_network(inputs_len, outputs_len, hidden_layers, 'sigmoid')


models = {} # one per number of hidden layers

def _get_neural_network(inputs_len, outputs_len, hidden_layers, output_activation):
    """Returns a neural network with the shape: 
        inputs, outputs, number hidden layers (without input and output layers)
        and the activation fuction for the output:
            - softmax: for multiclassification
            - sigmoid: for others
        """
    
    global models    # TODO: check singleton...
    if hidden_layers not in models: 
        models[hidden_layers] = Sequential() 
        if hidden_layers == 0:
            layer = Dense(outputs_len, input_dim=inputs_len, activation='softmax', kernel_initializer='zeros')
            models[hidden_layers].add(layer)
        elif hidden_layers == 1:
            layer = Dense(inputs_len, input_dim=inputs_len, activation='relu', kernel_initializer='zeros')  # we keep same input params lenght in the hidden layer
            layer_out = Dense(outputs_len, activation='softmax', kernel_initializer='zeros')
            models[hidden_layers].add(layer)
            models[hidden_layers].add(layer_out)
        elif hidden_layers == 2:
            layer = Dense(inputs_len, input_dim=inputs_len, activation='relu', kernel_initializer='zeros')  # we keep same input params lenght in the hidden layer
            layer_2 = Dense(inputs_len, activation='relu', kernel_initializer='zeros')
            layer_out = Dense(outputs_len, activation='softmax', kernel_initializer='zeros')
            models[hidden_layers].add(layer)
            models[hidden_layers].add(layer_2)
            models[hidden_layers].add(layer_out)
        else: raise Exception('No more than 2 hidden layers so far')
    return models[hidden_layers]

def _set_weights(model, weights):
    """load the weights in the neural network
    weights: 
     - first n-1 rows are the weights for each input
     - last row are the biases
    """
    # each layer weights and biases shape:   [ numpy array of weights, numpy array of biases]  
    # e.g inputs:8 outputs:3
    # w = [ 
    #     np.array(range(8*3)).reshape((8,3)),  # weights: 8 inputs, 3 outpus
    #     np.array(range(3))   # biases, 3 outputs
    #     ]
    # [array([[ 0,  1,  2],
    #    [ 3,  4,  5],
    #    [ 6,  7,  8],
    #    [ 9, 10, 11],
    #    [12, 13, 14],
    #    [15, 16, 17],
    #    [18, 19, 20],
    #    [21, 22, 23]]), array([0, 1, 2])]
    assert len(model.layers) == len(weights), "Number of layers don't correspond with weights: %s != %s" % (len(model.layers), len(weights))
    i = 0
    for layer in model.layers:
        _weights = np.array(weights[i][:-1])
        _biases = np.array(weights[i][-1])
        # print("get_weights", layer.get_weights())
        # print("_weights", [_weights, _biases])
        layer.set_weights([_weights, _biases])
        i += 1
    # return model - not needed

def _predict(model, inputs):
    res = model.predict(inputs)
    # print("_predict res:",res)
    return list(res[0]).index(max(res[0]))

def get_random_neurons_array(inputs_len, outputs_len, hidden_layers):
    rands_2 = tuple(random.random() for _ in range(outputs_len))
    l_2 = tuple(rands_2 for _ in range(inputs_len+1))
    if hidden_layers == 0:
        return (l_2,)  # hidden_layers == 0
    if hidden_layers == 1:
        rands_1 = tuple(random.random() for _ in range(inputs_len))
        l_1 = tuple(rands_1 for _ in range(inputs_len+1))
        return (l_1, l_2)
    raise Exception("Only ready for 0 or 1 hidden layer, sorry")

    