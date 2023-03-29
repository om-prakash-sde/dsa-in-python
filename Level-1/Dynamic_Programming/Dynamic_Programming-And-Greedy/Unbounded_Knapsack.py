"""
Unbounded Knapsack
===================

1. You are given a number n, representing the count of items.
2. You are given n numbers, representing the values of n items.
3. You are given n numbers, representing the weights of n items.
3. You are given a number "cap", which is the capacity of a bag you've.
4. You are required to calculate and print the maximum value that can be created in the bag without
    overflowing it's capacity.
Note -> Each item can be taken any number of times. You are allowed to put the same item again
                  and again.

sample input
============
5
15 14 10 45 30
2 5 1 3 4
7

sample output
=============
100

"""


def unbounded_knapSack(cap, wt, val, n):
    dp = [0 for i in range(cap + 1)]
    dp[0] = 0

    for bagc in range(1, cap + 1):
        maxv = 0
        for i in range(0, n):
            if wt[i] <= bagc:
                rbagc = bagc - wt[i]
                rbagv = dp[rbagc]
                tbagv = rbagv + val[i]

                if tbagv > maxv:
                    maxv = tbagv
        dp[bagc] = maxv

    return dp[cap]


n = int(input())
st1 = input()
v = st1.split()
val = [int(i) for i in v]
st2 = input()
w = st2.split()
wt = [int(j) for j in w]
cap = int(input())
print(unbounded_knapSack(cap, wt, val, n))
