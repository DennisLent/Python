def Bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


#lst = [6,7,1,5,6,8,2,21,5,3,7,9]
#print(BubbleSort(lst))