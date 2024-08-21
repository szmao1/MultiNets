import numpy as np
from similarity import intra_layer_similarity

def construct_feature_matrix(multiplex_networks):
    num_layers = len(multiplex_networks)
    num_nodes = len(multiplex_networks[0].nodes)
    feature_matrix = np.zeros((num_nodes, num_layers))
    
    for i in range(num_layers):
        feature_matrix[:, i] = np.sum(intra_layer_similarity(multiplex_networks[i]), axis=1)
    
    return feature_matrix
