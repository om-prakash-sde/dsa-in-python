"""
Min Cost In Maze Traversal
==========================
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a maze.
4. You are standing in top-left cell and are required to move to bottom-right cell.
5. You are allowed to move 1 cell right (h move) or 1 cell down (v move) in 1 motion.
6. Each cell has a value that will have to be paid to enter that cell (even for the top-left and bottom-right cell).
7. You are required to traverse through the matrix and print the cost of path which is least costly.

sample input
===========
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
23
"""


def fun(n, m, arr):
    dp = [[0 for c in range(m)] for r in range(n)]
    for i in range((len(dp) - 1), -1, -1):
        for j in range((len(dp[0]) - 1), -1, -1):
            if i == (len(dp) - 1) and j == (len(dp[0]) - 1):
                dp[i][j] = arr[i][j]
            elif i == len(dp) - 1:
                dp[i][j] = dp[i][j + 1] + arr[i][j]
            elif j == len(dp[0]) - 1:
                dp[i][j] = dp[i + 1][j] + arr[i][j]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + arr[i][j]
    return dp[0][0]


# driver code
def main():
    n = int(input())
    m = int(input())
    arr = []
    for i in range(0, n):
        ar = []
        l = input()
        for j in range(0, m):
            lst = l.split(" ")
            val = int(lst[j])
            ar.append(val)
        arr.append(ar)
    print(fun(n, m, arr))


if __name__ == "__main__":
    main()
