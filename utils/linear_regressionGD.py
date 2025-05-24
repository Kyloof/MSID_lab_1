import numpy as np
from sklearn.model_selection import KFold

class LinearRegressionGD:
    def __init__(self, learning_rate=0.001, iterations=100, batch_size=16,
                 regularization=None, lr_lambda=0.01):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.batch_size = batch_size
        self.regularization = regularization  # None, 'l1', 'l2'
        self.lr_lambda = lr_lambda
        self.theta = None
        self.mu = None
        self.sigma = None
        self.cost_history_train = []
        self.cost_history_val = []

    def _compute_cost(self, A, b):
        m = len(b)
        predictions = A.dot(self.theta)
        cost = (1 / (2 * m)) * np.sum((predictions - b) ** 2)

        if self.regularization == 'l2':
            cost += (self.lr_lambda / (2 * m)) * np.sum(self.theta[1:] ** 2)
        elif self.regularization == 'l1':
            cost += (self.lr_lambda / (2 * m)) * np.sum(np.abs(self.theta[1:]))
        return cost

    def _feature_normalize(self, A):
        self.mu = np.mean(A, axis=0)
        self.sigma = np.std(A, axis=0)
        return (A - self.mu) / self.sigma

    def _add_intercept(self, A):
        return np.c_[np.ones((A.shape[0], 1)), A]

    def fit(self, A_train, b_train, A_val=None, b_val=None):
        A_train_norm = self._feature_normalize(A_train)
        A_train_aug = self._add_intercept(A_train_norm)

        self.theta = np.zeros(A_train_aug.shape[1])

        if A_val is not None and b_val is not None:
            A_val_norm = (A_val - self.mu) / self.sigma
            A_val_aug = self._add_intercept(A_val_norm)
        else:
            A_val_aug = None

        self.cost_history_train = []
        self.cost_history_val = []

        m = len(b_train)

        for epoch in range(self.iterations):
            for j in range(0, m, self.batch_size):
                A_batch = A_train_aug[j:j + self.batch_size]
                b_batch = b_train[j:j + self.batch_size]

                predictions = A_batch.dot(self.theta)
                errors = predictions - b_batch
                gradient = (1 / len(b_batch)) * A_batch.T.dot(errors)

                reg_term = np.zeros_like(self.theta)
                if self.regularization == 'l2':
                    reg_term[1:] = (self.lr_lambda / len(b_batch)) * self.theta[1:]
                elif self.regularization == 'l1':
                    reg_term[1:] = (self.lr_lambda / len(b_batch)) * np.sign(self.theta[1:])

                gradient += reg_term

                self.theta -= self.learning_rate * gradient

            cost_train = self._compute_cost(A_train_aug, b_train)
            self.cost_history_train.append(cost_train)

            if A_val_aug is not None:
                cost_val = self._compute_cost(A_val_aug, b_val)
                self.cost_history_val.append(cost_val)

    def predict(self, A):
        A_norm = (A - self.mu) / self.sigma
        A_aug = self._add_intercept(A_norm)
        return A_aug.dot(self.theta)

    def cross_validate(self, A, b, k=3):
        kf = KFold(n_splits=k, shuffle=True, random_state=6)
        final_costs = []

        for i, (train_index, val_index) in enumerate(kf.split(A)):
            A_train, A_val = A.iloc[train_index], A.iloc[val_index]
            b_train, b_val = b.iloc[train_index], b.iloc[val_index]

            self.fit(A_train, b_train, A_val, b_val)

            final_val_cost = self.cost_history_val[-1] if self.cost_history_val else None
            print(f"\nFold {i+1} validation cost (MSE): {final_val_cost:.6f}")
            final_costs.append(final_val_cost)

        return np.mean(final_costs)
