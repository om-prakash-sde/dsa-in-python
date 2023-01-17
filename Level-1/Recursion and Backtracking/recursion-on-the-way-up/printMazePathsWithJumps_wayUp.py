"""
1. You are given a number n and a number m representing number of rows and columns in a maze.
2. You are standing in the top-left corner and have to reach the bottom-right corner. 
3. In a single move you are allowed to jump 1 or more steps horizontally (as h1, h2, .. ),
 or 1 or more steps vertically (as v1, v2, ..) or 1 or more 
steps diagonally (as d1, d2, ..). 
4. Complete the body of printMazePath function - without changing signature - to print the 
list of all paths that can be used to move from top-left to bottom-right.
Use sample input and output to take idea about output.

Note -> The online judge can't force you to write the function recursively but that is what
 the spirit of question is. Write recursive and not iterative logic. The purpose of the 
 question is to aid learning recursion and not test you.

"""


import sys
sys.setrecursionlimit (10000)

def printMazePathsWithJumps(sr, sc, dr, dc, asf):
    if dc==sc and dr==sr:
        print(asf)
        return
    for i in range(1,(dc-sc)+1):
        printMazePathsWithJumps(sr, sc+i, dr, dc, asf+"h"+str(i))
    
    for i in range(1,(dr-sr)+1):
        printMazePathsWithJumps(sr+i, sc, dr, dc, asf+"v"+str(i))
    
    for i in range(1,(dr-sr)+1):
        if i < (dc-sc)+1:
            printMazePathsWithJumps(sr+i, sc+i, dr, dc, asf+"d"+str(i))


def main():
    n = int(input())
    m = int(input())
    printMazePathsWithJumps(0, 0, n - 1, m - 1, "")
    
if __name__ == '__main__':
    main()