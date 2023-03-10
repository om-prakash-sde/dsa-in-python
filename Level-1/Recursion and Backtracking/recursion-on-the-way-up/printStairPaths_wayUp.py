"""
printStairPaths-recursion-on the way up
==================
1. You are given a number n representing number of stairs in a staircase.
2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 steps
 in one move.
3. Complete the body of printStairPaths function - without changing signature - to print the 
list of all paths that can be used to climb the staircase up.
Use sample input and output to take idea about output.

Note -> The online judge can't force you to write the function recursively but that is what the 
spirit of question is. Write recursive and not iterative 
logic. The purpose of the question is to aid learning recursion and not test you.
"""



def printStairPaths(ques, asf):
    if ques < 0:
        return
    if ques == 0:
        print(asf)
        return
    printStairPaths(ques-1,asf+"1")
    printStairPaths(ques-2,asf+"2")
    printStairPaths(ques-3,asf+"3")
    

def main():
    ques = int(input())
    printStairPaths(ques, "");
    
if __name__ == '__main__':
    main()