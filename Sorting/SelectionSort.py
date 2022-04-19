def Selection_sort(lst):
    sorted_list = []
    while len(lst) != 0:
        sml = min(lst)
        sorted_list.append(sml)
        lst.remove(sml)
    return sorted_list
