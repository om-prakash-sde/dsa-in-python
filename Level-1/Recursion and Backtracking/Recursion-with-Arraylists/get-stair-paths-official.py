'''
1. You are given a number n representing number of stairs in a staircase.
2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 
steps in one move.
3. Complete the body of getStairPaths function - without changing signature - to get the list of
 all paths that can be used to climb the staircase up.
Use sample input and output to take idea about output.

Note -> The online judge can't force you to write the function recursively but that is what the
 spirit of question is. Write recursive and not iterative 
logic. The purpose of the question is to aid learning recursion and not test you.
'''

def get_stair_paths(n):
    if n==0:
        return [""]
    elif n<0:
        return []
    path1=get_stair_paths(n-1)
    path2=get_stair_paths(n-2)
    path3=get_stair_paths(n-3)
    pathr=[]
    
    for i in path1:
        pathr.append('1'+i)
    for i in path2:
        pathr.append('2'+i)
    for i in path3:
        pathr.append('3'+i)
    return pathr
    

def main():
    n = int(input())
    ans = get_stair_paths(n)
    print("[" + ', '.join(ans) + "]")

main()