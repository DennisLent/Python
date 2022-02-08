def Quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        left, right, mid = [], [], []
        pivot = lst[0]
        for elem in lst:
            if elem < pivot:
                left.append(elem)
            elif elem > pivot:
                right.append(elem)
            else:
                mid.append(elem)

        if len(left) > 1:
            left = Quick_sort(left)

        if len(right) > 1:
            right = Quick_sort(right)

        return left + mid + right


#lst = [2,8,7,1,3,5,32,67,21,4,1,7,9,4,21,3,5,7,8]
#print(Quick_sort(lst))
