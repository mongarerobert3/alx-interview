#!/usr/bin/python3
"""number of copy and paste given a number"""


def minOperations(n):
    '''Checking the minimum operations that can be done'''
    current = 1
    num_copied = 0
    steps = 0
    while current < n:
        rest = n - current
        if (rest % current == 0):
            num_copied = current
            current += num_copied
            steps += 2
        else:
            current += num_copied
            steps += 1
    return steps
