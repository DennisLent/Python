import numpy as np
import scipy as sp
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
    """take around 70% for training"""
    training_data = []
    testing_data = []
    classification = []
    data_numbered = enumerate(data_set)
    n = round(len(data_set[0])*0.7)
    for index, lst in data_numbered:
        train = lst[:n]
        test = lst[n:]
        training_data += train
        testing_data += test
        classification += f"{index}"*n
    return training_data, testing_data, classification




data = generate_random_data(8, 20, -100, 100)
print(data)
graph_data(data)

train, test, c = split_data(data)
print(train)
print(test)
print(classification)


def KNN(point):
    pass


