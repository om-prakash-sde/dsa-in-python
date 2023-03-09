"""
Goldmine
========
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a gold mine.
4. You are standing in front of left wall and are supposed to dig to the right wall. You can start from
     any row in the left wall.
5. You are allowed to move 1 cell right-up (d1), 1 cell right (d2) or 1 cell right-down(d3).
6. Each cell has a value that is the amount of gold available in the cell.
7. You are required to identify the maximum amount of gold that can be dug out from the mine.

sample input
============
6
6
0 1 4 2 8 2
4 3 6 5 0 4
1 2 4 1 4 6
2 0 7 3 2 2
3 1 5 9 2 4
2 7 0 8 5 1

sample output
=============
33
"""


def fun(n, m, mine):
    dp = [[0 for c in range(m)] for r in range(n)]
    # write code here
    for j in range(m - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            if j == m - 1:
                dp[i][j] = mine[i][j]
            elif i == n - 1:
                dp[i][j] = mine[i][j] + max(dp[i][j + 1], dp[i - 1][j + 1])
            elif i == 0:
                dp[i][j] = mine[i][j] + max(dp[i][j + 1], dp[i + 1][j + 1])
            else:
                dp[i][j] = mine[i][j] + max(dp[i][j + 1], dp[i + 1][j + 1], dp[i - 1][j + 1])

    maxi = dp[0][0]
    for i in range(1, n - 1):
        if dp[i][0] > maxi:
            maxi = dp[i][0]
    return maxi


# driver code
def main():
    n = int(input())
    m = int(input())
    mine = []
    for i in range(0, n):
        a = []
        l = input()
        for j in range(0, m):
            lst = l.split(" ")
            val = int(lst[j])
            a.append(val)
        mine.append(a)
    print(fun(n, m, mine))


if __name__ == "__main__":
    main()
