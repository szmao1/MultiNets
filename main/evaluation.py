from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate_model(predictions, true_values):
    mae = mean_absolute_error(true_values, predictions)
    rmse = mean_squared_error(true_values, predictions, squared=False)
    mape = np.mean(np.abs((true_values - predictions) / true_values)) * 100
    
    print(f'MAE: {mae}')
    print(f'RMSE: {rmse}')
    print(f'MAPE: {mape}%')
    
    return mae, rmse, mape