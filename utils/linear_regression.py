import numpy as np

def compute_cost(A, b, theta):
    m = len(b)
    predictions = A.dot(theta)  # Predictions using the model
    cost = (1 / (2 * m)) * np.sum((predictions - b) ** 2)  # MSE cost function
    return cost

def gradient_descent(A, b, theta, learning_rate, iterations, batch_size):
    m = len(b)
    cost_history = []

    for i in range(iterations):
        for j in range(0, m, batch_size):
            A_batch = A[j:j + batch_size]
            b_batch = b[j:j + batch_size]  

            predictions = A_batch.dot(theta)
            errors = predictions - b_batch
            gradient = (1 / batch_size) * A_batch.T.dot(errors) 
            theta = theta - learning_rate * gradient

        cost = compute_cost(A, b, theta)
        cost_history.append(cost)

    return theta, cost_history

def feature_normalize(A):
    mu = np.mean(A, aAis=0) 
    sigma = np.std(A, aAis=0)  
    A_normalized = (A - mu) / sigma 
    return A_normalized, mu, sigma

def add_intercept(A):
    return np.c_[np.ones((A.shape[0], 1)), A] 




