"""
Zero One Knapsack
==================

1. You are given a number n, representing the count of items.
2. You are given n numbers, representing the values of n items.
3. You are given n numbers, representing the weights of n items.
3. You are given a number "cap", which is the capacity of a bag you've.
4. You are required to calculate and print the maximum value that can be created in
the bag without overflowing it's capacity.

Note -> Each item can be taken 0 or 1 number of times. You are not allowed to put the same item
               again and again.

sample input
============
5
15 14 10 45 30
2 5 1 3 4
7

sample output
===========
75
"""


def zeroknapSack(cap, wt, val, n):
    dp = [[0 for i in range(cap + 1)] for j in range(n + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i - 1][j]
            if j >= wt[i - 1]:
                rcap = j - wt[i - 1]
                if (dp[i - 1][rcap] + val[i - 1]) > dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][rcap] + val[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][cap]


n = int(input())
st1 = input()
v = st1.split()
val = [int(i) for i in v]
st2 = input()
w = st2.split()
wt = [int(j) for j in w]
cap = int(input())
print(zeroknapSack(cap, wt, val, n))


