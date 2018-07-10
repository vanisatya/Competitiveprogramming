import unittest

def find_repeat(array):
    # Find a number that appears more than once
    for i in range(0, len(array)):
        if array[abs(array[i])] >= 0:
            array[abs(array[i])] = -array[abs(array[i])]
        else:
            return abs(array[i])

