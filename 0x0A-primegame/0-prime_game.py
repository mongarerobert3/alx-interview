#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
    """Determine if a player wins a game of prime numbers"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    prime_nums = [i for i in range(n + 1) if primes[i]]
    count = 0
    for num in nums:
        if num in prime_nums:
            count += 1
    if count * 2 == x:
        return None
    if count * 2 > x:
        return "Maria"
    return "Ben"
