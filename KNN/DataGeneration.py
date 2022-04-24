import random
import numpy as np
import matplotlib.pyplot as plt


def generate_random_data(num_sets, num_points, *, min_val=-50, max_val=50, std=2, classes=None):
    total_data = []
    if classes is not None and len(classes) != num_sets:
        return "Number of class names has to equal number of sets"

    for i in range(num_sets):
        x_center, y_center = random.randint(min_val, 0), random.randint(0, max_val)
        x_cords = np.random.normal(x_center, std, num_points)
        y_cords = np.random.normal(y_center, std, num_points)
        if classes is not None:
            subset = list(zip(x_cords, y_cords, [classes[i]]*num_points))
        else:
            subset = list(zip(x_cords, y_cords, [i]*num_points))

        total_data.append(subset)
    return total_data


if __name__ == "__main__":
    data = generate_random_data(8, 50)

    for subset in data:
        # print(subset)

        x, y, name = zip(*subset)
        plt.scatter(x, y, label=name[0])

    plt.legend()
    plt.show()
