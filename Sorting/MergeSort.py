import random
import sys

def Merge_sort(lst):

    def merge(left, right):
        if left[0] < right[0]:
            de_head, other = left, right
        else:
            de_head, other = right, left

        head, *tail = de_head

        if not tail:
            return [head] + other

        else:
            return [head] + merge(tail, other)

    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left, right = lst[:mid], lst[mid:]
        left = Merge_sort(left)
        right = Merge_sort(right)
        return merge(left, right)
