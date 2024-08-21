from graphs import create_multiplex_visibility_networks
from feature_matrix import construct_feature_matrix
from cnn_model import create_cnn_model
from decomposition import apply_emd

if __name__ == "__main__":
    external_factors = load_data()
    
    # Create multiplex visibility networks
    multiplex_networks = create_multiplex_visibility_networks(external_factors)
    feature_matrix = construct_feature_matrix(multiplex_networks)
    
    feature_matrix_expanded = np.expand_dims(feature_matrix, axis=-1)
    
    input_shape = (feature_matrix.shape[0], feature_matrix.shape[1], 1)
    model = create_cnn_model(input_shape)
    model.fit(train_X, train_Y, epochs=10, batch_size=32)
    predictions = model.predict(test_X)
