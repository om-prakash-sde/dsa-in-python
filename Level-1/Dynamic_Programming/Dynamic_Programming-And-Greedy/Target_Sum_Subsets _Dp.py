"""
Target Sum Subsets - Dp
==========================
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are given a number "tar".
4. You are required to calculate and print true or false, if there is a subset the elements of which add
     up to "tar" or not.

sample input
============
5
4
2
7
1
3
10

sample output
=============
true
"""


def targetsum(n, arr, tar, dp):
    #  write your code here
    for i in range(0, len(dp)):
        for j in range(0, len(dp[0])):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j == 0:
                dp[i][j] = True
            else:
                if dp[i - 1][j] == True:
                    dp[i][j] = True
                else:
                    val = arr[i - 1]
                    if j >= val:
                        if dp[i - 1][j - val] == True:
                            dp[i][j] = True
    print(str((dp[len(arr)][tar])).lower())


n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
tar = int(input())
dp = [[False for x in range(tar + 1)] for y in range(n + 1)]
targetsum(n, arr, tar, dp)
