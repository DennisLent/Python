import numpy as np
from statistics import mode
import matplotlib.pyplot as plt
import random

def generate_random_data(num_sets, num_points, low=-50, high=50):
    """Make random data sets"""
    data_sets = []
    for i in range(num_sets):
        lower_x, lower_y = random.randrange(low, 0), random.randrange(low, 0)
        upper_x, upper_y = random.randrange(0, high), random.randrange(0, high)
        x_cord = [random.randrange(lower_x, upper_x) for j in range(num_points)]
        y_cord = [random.randrange(lower_y, upper_y) for k in range(num_points)]
        data = list(zip(x_cord, y_cord))
        data_sets.append(data)
    return data_sets

def graph_data(data_set):
    """graph data sets"""
    for sub_set in data_set:
        x, y = zip(*sub_set)
        plt.scatter(x,y)
    plt.show()

def split_data(data_set):
    """take around 70% of the data for training"""
    training_data = []
    testing_data = []
    classification_test = []
    classification_train = []
    data_numbered = enumerate(data_set)
    n = round(len(data_set[0])*0.7)
    for index, lst in data_numbered:
        train = lst[:n]
        test = lst[n:]
        training_data += train
        testing_data += test
        classification_train += f"{index}"*n
        classification_test += f"{index}"*(len(data_set[0])-n)
    return training_data, classification_train, testing_data, classification_test

def distance(tup1, tup2):
    """Euclidian distance between two points"""
    x1, y1 = tup1
    x2, y2 = tup2
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

def KNN(data, point, k):
    """Find k points that are closest to given point in the data"""
    if k > len(data):
        raise ValueError("k has to be smaller than length of data set")

    closest = []
    while len(closest) < k:
        sml = np.inf
        smallest = None
        for cord in data:
            #print(distance(cord, point))
            if distance(cord, point) < sml:
                sml = distance(cord, point)
                smallest = cord
        closest.append(smallest)
        data.remove(smallest)
    return closest


def test_KNN(train, c_train, test, c_test, k):
    """Test how well the KNN works with guessing"""
    i = 0
    true = 0
    for test_point in test:
        neighbors = KNN(train.copy(), test_point, k)
        classes = []
        for neigh in neighbors:
            ind = train.index(neigh)
            classes.append(c_train[ind])
        guess = mode(classes)
        if guess == c_test[i]:
            true += 1
        #print(f"Guessed that point {test_point} is class {guess}; actual class {c_test[i]}")
        i += 1
    correct = true/i
    return correct




data = generate_random_data(5, 20)
graph_data(data)
train, c_train, test, c_test = split_data(data)


def Cross_fold_test(k_range, data):
    """Determine best value of k when taking 70% of data to train"""
    scores = []
    for k in k_range:
        train, c_train, test, c_test = split_data(data)
        score = test_KNN(train, c_train, test, c_test, k)
        print(f"k value of {k} scored {score*100}%")
        scores.append(score)
    plt.plot(k_range, scores)
    plt.show()


Cross_fold_test(range(1,15), data)








