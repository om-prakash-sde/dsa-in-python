"""
All Indices Of Array
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are given a number x. 
4. You are required to find the all indices at which x occurs in array a.
5. Return an array of appropriate size which contains all indices at which x occurs in array a.

Note -> The online judge can't force you to write the function recursively but that is what the spirit
 of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning 
 recursion and not test you.

"""

import sys
sys.setrecursionlimit (10000)

def allIndices(arr,x,idx,fsf):
    if idx==len(arr):
        return [0]*fsf
    iarr=[]
    if arr[idx]==x:
        iarr=allIndices(arr,x,idx+1,fsf+1)
        iarr[fsf]=idx
    else:
        iarr=allIndices(arr,x,idx+1,fsf)
    return iarr

def main():
    n = int(input())
    arr = []
    for i in range(n) :
        arr.append(int(input()))
    x = int(input())
    ans = allIndices(arr, x,0,0)
    if len(ans)==0:
        print()
    else:
        for i in ans:
            print(i)

main()