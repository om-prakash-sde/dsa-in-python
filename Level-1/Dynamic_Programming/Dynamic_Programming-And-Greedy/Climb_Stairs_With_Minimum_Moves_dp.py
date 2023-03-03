"""
++++++++++++++++++++ Climb Stairs With Minimum Moves++++++++++++++++++++

1. You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. You are given n numbers, where ith element's value represents - till how far from the step you
     could jump to in a single move.  You can of-course fewer number of steps in the move.
4. You are required to print the number of minimum moves in which you can reach the top of
     staircase.
Note -> If there is no path through the staircase print null.

"""

import sys


def fun(n, arr, dp):
    # write code here
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        if arr[i] > 0:
            minm = sys.maxsize
            for j in range(1, (arr[i] + 1)):
                if i + j < len(dp):
                    if dp[i + j] != None:
                        minm = min(minm, dp[i + j])
            if minm != sys.maxsize:
                dp[i] = minm + 1
    return dp[0]


# driver code
def main():
    n = int(input())
    jumps = []
    for i in range(n):
        jumps.append(int(input()))
    dp = [None] * (n + 1)
    ans = fun(n, jumps, dp)
    print(ans)
    # if (ans < 30):
    #     print(ans)
    # else:
    #     print("null")


if __name__ == "__main__":
    main()


"""
Sample input-
10
3
3
0
2
1
2
4
2
0
0

sample output-
4

"""