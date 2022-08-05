"""Implementations of some sorting"""
import random


def merge(a0, a1, a):
    i_0 = 0
    i_1 = 0

    for i in range(0, len(a)):

        if i_0 == len(a0):
            a[i] = a1[i_1]
            i_1 += 1

        elif i_1 == len(a1):
            a[i] = a0[i_0]
            i_0 += 1

        elif a0[i_0] < a1[i_1]:
            a[i] = a0[i_0]
            i_0 += 1

        else:
            a[i] = a1[i_1]
            i_1 += 1

def merge_sort(a):
    if len(a) <= 1:
        return a

    m = len(a) // 2
    a0 = merge_sort(a[0 : m])
    a1 = merge_sort(a[m : len(a)])
    merge(a0, a1, a)

    return a

def _quick_sort(a, i, n):
    if n <= 1:
        return

    x = a[i + random.randint(0, n - 1)]
    p = i - 1
    j = i
    q = i + n

    while j < q:

        if a[j] < x:
            p += 1
            a[j], a[p] = a[p], a[j]
            j += 1

        elif a[j] > x:
            q -= 1
            a[j], a[q] = a[q], a[j]

        else:
            j += 1

    _quick_sort(a, i, (p - i + 1))
    _quick_sort(a, q, (n - (q - i)))

def quick_sort(a):
    _quick_sort(a, 0, len(a))
    return a

def binary_search(a, x) :
    # lower_index = 0
    # higher_index = len(a) - 1
    #
    # while lower_index <= higher_index:
    #     midpoint = lower_index + (higher_index - lower_index) // 2
    #     midpoint_value = a[midpoint]
    #     if midpoint_value == x:
    #         return midpoint
    #
    #     elif x < midpoint_value:
    #         higher_index = midpoint - 1
    #
    #     else:
    #         lower_index = midpoint + 1
    #
    # return lower_index

    left_end = 0
    right_end = len(a) - 1

    while right_end > left_end:
        midpoint = (left_end + right_end) // 2

        if a[midpoint] == x:
            return midpoint

        elif x <= a[midpoint]:
            right_end = midpoint

        else:
            left_end = midpoint + 1


    return left_end

