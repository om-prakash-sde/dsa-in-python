"""
Flood Fill
==========
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a.
The numbers can be 1 or 0 only.
4. You are standing in the top-left corner and have to reach the bottom-right corner. 
Only four moves are allowed 't' (1-step up), 'l' (1-step left), 'd' (1-step down) 'r' 
(1-step right). You can only move to cells which have 0 value in them. You can't move
 out of the boundaries or in the cells which have value 1 in them (1 means obstacle)
5. Complete the body of floodfill function - without changing signature - to print all
 paths that can be used to move from top-left to bottom-right.

Note1 -> Please check the sample input and output for details
Note2 -> If all four moves are available make moves in the order 't', 'l', 'd' and 'r'
"""

import sys
sys.setrecursionlimit(100000)

# asf -> answer so far
def floodfill(maze, sr, sc, asf,visited):
    if (sr < 0 or sc < 0 or sr == len(maze) or sc == len(maze[0]) or maze[sr][sc]==1 or visited[sr][sc] == True):
        return
    
    if sr == (len(maze)-1) and sc == (len(maze[0])-1):
        print(asf)
        return
    
    visited[sr][sc] = True
    floodfill(maze,sr-1,sc,asf+"t",visited)
    floodfill(maze,sr,sc-1,asf+"l",visited)
    floodfill(maze,sr+1,sc,asf+"d",visited)
    floodfill(maze,sr,sc+1,asf+"r",visited)
    visited[sr][sc] = False
    
    
def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    arr = []
    for i in range(n) :
        row = list(map(int, input().split()))
        arr.append(row)
    visited=[]
    for i in range(n) :
        v=[]
        for j in range(m):
            v.append(bool(False))
        visited.append(v)
    floodfill(arr, 0, 0, "",visited)
    
if __name__ == '__main__':
    main()