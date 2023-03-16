"""
Coin Change Combination
=========================
1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the number of combinations of the n coins using which the
     amount "amt" can be paid.

Note1 -> You have an infinite supply of each coin denomination i.e. same coin denomination can be
                  used for many installments in payment of "amt"
Note2 -> You are required to find the count of combinations and not permutations i.e.
                  2 + 2 + 3 = 7 and 2 + 3 + 2 = 7 and 3 + 2 + 2 = 7 are different permutations of same
                  combination. You should treat them as 1 and not 3.

sample input
-------------
4
2
3
5
6
7

sample output
--------------
2
"""


def coinComb(n, arr, amt):
    dp = [0 for i in range(0, (amt + 1))]
    dp[0] = 1
    for i in range(0, n):
        for j in range(arr[i], len(dp)):
            dp[j] += dp[j - arr[i]]
    return dp[amt]


def main():
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    amt = int(input())
    print(coinComb(n, arr, amt))


if __name__ == '__main__':
    main()
