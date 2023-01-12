# Last index-recursion
"""
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are given a number x. 
4. You are required to find the last index at which x occurs in array a.
5. If x exists in array, print the last index where it is found otherwise print -1.

Note -> The online judge can't force you to write the function recursively but that is what 
the spirit of question is. Write recursive and not iterative logic. 
The purpose of the question is to aid learning recursion and not test you.
"""


import sys
sys.setrecursionlimit (10000)

def Lastindex(arr, idx, x, n):
    if idx==n:
        return -1
    liisa = Lastindex(arr,idx+1,x,n)
    if liisa ==-1:
        if arr[idx]==x:
            return idx
        else:
            return -1
    else:
        return liisa

def main():
    n = int(input())
    arr = []
    for i in range(n) :
        arr.append(int(input()))
    x = int(input())
    ans = Lastindex(arr, 0, x, n)
    print(ans)
main()

# code by omprakash