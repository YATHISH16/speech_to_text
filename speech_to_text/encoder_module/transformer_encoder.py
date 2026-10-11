import numpy as np

def transformer_encode(features):

    encoded = np.tanh(features)

    return encoded