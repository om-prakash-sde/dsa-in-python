"""
Coin Change Permutations
=========================

1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the number of permutations of the n coins using which the
     amount "amt" can be paid.

Note1 -> You have an infinite supply of each coin denomination i.e. same coin denomination can be
                  used for many installments in payment of "amt"
Note2 -> You are required to find the count of permutations and not combinations i.e.
                  2 + 2 + 3 = 7 and 2 + 3 + 2 = 7 and 3 + 2 + 2 = 7 are different permutations of same
                  combination. You should treat them as 3 and not 1.


sample input
============
4
2
3
5
6
7

sample output
=============
5

"""


def coin_perm(n, arr, amt):
    dp = [0 for i in range(0, (amt + 1))]
    # possible case at 0th position is always one
    dp[0] = 1

    for i in range(1, len(dp)):
        for j in arr:
            if j <= i:
                # ramt - remaining amount
                ramt = i - j
                dp[i] += dp[ramt]

    return dp[amt]


def main():
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    amt = int(input())
    print(coin_perm(n, arr, amt))


if __name__ == '__main__':
    main()
