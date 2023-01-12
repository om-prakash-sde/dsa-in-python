"""
Get Maze Path With Jumps
========================
1. You are given a number n and a number m representing number of rows and columns in a maze.
2. You are standing in the top-left corner and have to reach the bottom-right corner. 
3. In a single move you are allowed to jump 1 or more steps horizontally (as h1, h2, .. ), 
or 1 or more steps vertically (as v1, v2, ..) or 1 or
 more steps diagonally (as d1, d2, ..). 
4. Complete the body of getMazePath function - without changing signature - to get the list
 of all paths that can be used to move from top-left to bottom-right.
Use sample input and output to take idea about output.

Note -> The online judge can't force you to write the function recursively but that is what
 the spirit of question is. Write recursive and not iterative logic. The purpose of the
  question is to aid learning recursion and not test you.
"""



def get_maze_paths(sr, sc, dr, dc):
    if sr==dr and sc==dc:
        return [""]
    
    res=[]
    for i in range(1,((dc-sc)+1)):
        hpath=get_maze_paths(sr,sc+i,dr,dc)
        for j in hpath:
            res.append('h'+str(i)+j)
    
    for i in range(1,((dr-sr)+1)):
        vpath=get_maze_paths(sr+i,sc,dr,dc)
        for j in vpath:
            res.append('v'+str(i)+j)
    
    for i in range(1,((dc-sc)+1)):
        if i < ((dr-sr)+1):
            dpath=get_maze_paths(sr+i,sc+i,dr,dc)
            for j in dpath:
                res.append('d'+str(i)+j)
    return res

def main():
    n = int(input())
    m = int(input())
    ans = get_maze_paths(0, 0, n-1, m-1)
    print("["+', '.join(ans) + "]")

main()