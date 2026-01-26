
import numpy as np


def create_train_dataset():
    n_train = 100000
    max_train_card = 10

    X_train = np.empty(n_train, dtype=object)
    y_train = np.empty(n_train, dtype=int)

    for i in range(n_train):
        length = np.random.randint(1, max_train_card + 1)
        x = np.zeros(10)
        for j in range(length) :
            x[j] = np.random.randint(1, 11)
        X_train[i] = x
        y_train[i] = np.sum(x)

    return X_train, y_train


def create_test_dataset():
    
    n_train = 20
    X_test = []
    y_test = []
    for i in range(n_train) :
        X_current = []
        y_current = []
        length = (i+1)*5
        for _ in range(10_000) :
            x = np.random.randint(1, 11, size=length)
            X_current.append(x)
            y_current.append(np.sum(x))
        X_current = np.array(X_current, dtype=object)
        y_current = np.array(y_current)

        X_test.append(X_current)
        y_test.append(y_current)

    return X_test, y_test
