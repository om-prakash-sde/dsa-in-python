"""
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are given a number "tar".
4. Complete the body of printTargetSumSubsets function - without changing signature - 
to calculate and print all subsets of given elements, the contents of which sum to "tar".
 Use sample input and output to get more idea.

Note -> The online judge can't force you to write the function recursively but that is
 what the spirit of question is. Write recursive and not iterative logic. The purpose of 
 the question is to aid learning recursion and not test you.
"""

import sys
sys.setrecursionlimit(10000000)
# asf is the subset
# sos is sum of subset
# tar is target
def printTargetSumSubsets(arr, idx, asf, sos, tar):
    if idx == (len(arr)):
        if sos == tar:
            print(asf+".")
        return
    printTargetSumSubsets(arr,idx+1,asf+str(arr[idx])+", ",sos+arr[idx],tar)
    printTargetSumSubsets(arr,idx+1,asf,sos,tar)

def main():
    n = int(input())
    arr = []
    for i in range(n) :
        arr.append(int(input()))
    tar = int(input())
    printTargetSumSubsets(arr,0,"",0,tar)


if __name__ == '__main__':
    main()