#Print Subsequence
"""
1. You are given a string str.
2. Complete the body of printSS function - without changing signature -
 to calculate and print all subsequences of str.
Use sample input and output to take idea about subsequences.

Note -> The online judge can't force you to write the function recursively
 but that is what the spirit of question is. Write recursive and not 
 iterative logic. The purpose of the question is to aid learning recursion 
 and not test you.
"""


def printSS(ques,ans):
    if len(ques) == 1:
        print(ans)
        return
    ch=ques[0]
    ros=ques[1:]
    printSS(ros,ans+ch)
    printSS(ros,ans+'')

def main():
    s=input()
    printSS(s,"")
    
if __name__ == "__main__":
    main()