# ########### Climb Stairs With Variable Jumps ################
"""

1. You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. You are given n numbers, where ith element's value represents - till how far from the step you
     could jump to in a single move.
     You can of course jump fewer number of steps in the move.
4. You are required to print the number of different paths via which you can climb to the top.
"""


def fun(n, arr, dp):
    # write code here
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        for j in range(1, (arr[i] + 1)):
            if i + j < len(dp):
                dp[i] += dp[i + j]
    return dp[0]


# driver code
def main():
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    dp = [0] * (n + 1)
    print(fun(n, arr, dp))


if __name__ == "__main__":
    main()

"""
sample input
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
output-
5
"""