"""
Count Binary Strings
=====================

1. You are given a number n.
2. You are required to print the number of binary strings of length n with no consecutive 0's.


sample input
=============
6

sample output
=============
21

"""


def count_binary_strings(n):
    ocones = 1
    oczeros = 1

    for i in range(2, n + 1):
        nczeros = ocones
        ncones = oczeros + ocones

        ocones = ncones
        oczeros = nczeros

    return ocones + oczeros


if __name__ == '__main__':
    n = int(input())
    res = count_binary_strings(n)
    print(res)
