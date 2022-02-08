import matplotlib.pyplot as plt
from time import process_time
from BubbleSort import Bubble_sort
from MergeSort import Merge_sort
from QuickSort import Quick_sort
import random
import numpy as np


funclist = [Bubble_sort, Merge_sort, Quick_sort]
func_times = []
for function in funclist:
    print(f"---Testing {function}---")
    times = []
    for list_length in range(10, 10000, 1000):
        trial_time = []
        for trial in range(5):
            print(f"---Starting trial {trial + 1}---")
            lst = [random.randint(-50, 50) for i in range(list_length)]
            t1 = process_time()
            function(lst)
            t2 = process_time()
            time = t2 - t1
            trial_time.append(time)
            print(f"...trial finished with a time of {time} [s]")
        final_time = np.mean(trial_time)
        times.append(final_time)
    func_times.append(times)

for i in range(len(funclist)):
    plt.plot([i for i in range(10, 10010, 100)], func_times[i], label=f"{funclist[i]}")

plt.legend()
plt.show()
