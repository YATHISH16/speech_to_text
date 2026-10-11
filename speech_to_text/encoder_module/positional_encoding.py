import numpy as np

def add_position_encoding(features):

    rows, cols = features.shape

    position = np.arange(cols)

    features = features + position

    return features