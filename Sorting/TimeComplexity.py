import matplotlib.pyplot as plt
from time import process_time_ns
from BubbleSort import Bubble_sort
from MergeSort import Merge_sort
from QuickSort import Quick_sort
from SelectionSort import Selection_sort
from InsertionSort import Insertion_sort
import random
import numpy as np
import sys

class recursionlimit:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)

funclist = [Merge_sort, Bubble_sort, Selection_sort, Quick_sort, Insertion_sort]
func_times = []
test_range = range(10,3000,100)

with recursionlimit(5000):
    for function in funclist:
        print(f"---Testing {function}---")
        times = []
        for list_length in test_range:
            print(f"---Testing list with {list_length} elements---")
            trial_time = []
            for trial in range(10):
                print("."*(trial+1) + f"{trial + 1}")
                lst = [random.randint(-50, 50) for i in range(list_length)]
                t1 = process_time_ns()
                sorted_list = function(lst)
                t2 = process_time_ns()
                time = t2 - t1
                if sorted_list == sorted(lst):
                    print(f"Sorted!")
                else:
                    print("Issue sorting")
                trial_time.append(time)
                #print(f"...trial finished with a time of {time} [s]")
            final_time = np.mean(trial_time)
            times.append(final_time)
        func_times.append(times)

    for i in range(len(funclist)):
        plt.plot([i for i in test_range], func_times[i], label=f"{funclist[i].__name__}")

    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.title(f"Run Time of Sorting Algorithms")
    plt.ylabel(f"Average Time [nanoseconds]")
    plt.xlabel(f"Array Length")
    plt.show()
