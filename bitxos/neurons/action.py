import collections


def get_actions( quadrants, state, memory, network):
    """Neural network to decide next action based on what is around, current state and memory"""

    print("quadrants", quadrants, "state", state)
    res = networks._predict( network, quadrants.extend(state))

    return res, state
    