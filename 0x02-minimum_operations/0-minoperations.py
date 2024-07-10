#!/usr/bin/env python3
""" min op problem """

def minOperations(n):
    """
    Calculate the minimum number of operations needed to result in exactly n 'H' characters in the file.
    
    You can perform two operations on a file containing a single character 'H':
    1. Copy All
    2. Paste

    Args:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required to reach exactly n 'H' characters.
         Returns 0 if n is impossible to achieve.

    Example:
    >>> minOperations(9)
    6
    Explanation: The operations are:
    - Start with 1 'H'
    - Copy All and Paste (now 2 'H')
    - Paste (now 3 'H')
    - Copy All and Paste (now 6 'H')
    - Paste (now 9 'H')
    - Total operations: 6

    >>> minOperations(12)
    7
    Explanation: The operations are:
    - Start with 1 'H'
    - Copy All and Paste (now 2 'H')
    - Copy All and Paste (now 4 'H')
    - Copy All and Paste twice (now 12 'H')
    - Total operations: 7
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
