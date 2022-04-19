def Insertion_sort(lst):
    for i in range(len(lst)):
        key = lst[i]

        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst
