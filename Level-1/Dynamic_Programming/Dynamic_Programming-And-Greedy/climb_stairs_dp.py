"""
Climb Stairs
=============
1. You are given a number n, representing the number of stairs in a 
staircase.
2. You are on the 0th step and are required to climb to the top.
3. In one move, you are allowed to climb 1, 2 or 3 stairs.
4. You are required to print the number of different paths via which you
 can climb to the top.

"""


# By using tabulation.

def fun(n, dp):
    # write code here
    dp[0] = 1
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = dp[i - 1]
        elif i == 2:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


# driver code
def main():
    n = int(input())
    dp = [0] * (n + 1)
    print(fun(n, dp))


if __name__ == "__main__":
    main()

# checked with input ===3 output ==7
