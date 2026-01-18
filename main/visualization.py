import matplotlib.pyplot as plt

def plot_predictions(true_values, predictions):
    plt.figure(figsize=(10, 6))
    plt.plot(true_values, label='Actual Prices')
    plt.plot(predictions, label='Predicted Prices')
    plt.xlabel('Time')
    plt.ylabel('Carbon Price')
    plt.legend()
    plt.title('Actual vs Predicted Carbon Prices')
    plt.show()