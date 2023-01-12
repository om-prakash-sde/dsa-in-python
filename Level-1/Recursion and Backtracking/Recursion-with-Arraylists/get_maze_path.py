"""
Get Maze Paths
==============
1. You are given a number n and a number m representing number of rows and columns in a maze.
2. You are standing in the top-left corner and have to reach the bottom-right corner. Only two 
moves are allowed 'h' (1-step horizontal) and 'v' (1-step vertical).
3. Complete the body of getMazePath function - without changing signature - to get the list of 
all paths that can be used to move from top-left to bottom-right.
Use sample input and output to take idea about output.

Note -> The online judge can't force you to write the function recursively but that is what the
 spirit of question is. Write recursive and not iterative logic. 
The purpose of the question is to aid learning recursion and not test you.
"""


def get_maze_path(sr, sc, dr, dc):
    if sr==dr and sc==dc:
        return [""]
    hpath=[]
    vpath=[]
    if sc<dc:
        hpath=get_maze_path(sr,sc+1,dr,dc)
    if sr<dr:
        vpath=get_maze_path(sr+1,sc,dr,dc)
    res=[]
    for i in hpath:
        res.append('h'+i)
    for i in vpath:
        res.append('v'+i)
    return res


def main():
    n = int(input())
    m = int(input())
    ans = get_maze_path(0, 0, n - 1, m - 1)
    print("[" + ', '.join(ans) + "]")
    
main()