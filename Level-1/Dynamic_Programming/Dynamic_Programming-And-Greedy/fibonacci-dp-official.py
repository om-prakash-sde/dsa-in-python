'''
Dynamic programming
=====================
*****Fibonacci-dp*****
======================
1. You are given a number n.
2. You are required to print the nth element of fibonnaci sequence.

Note -> Notice precisely how we have defined the fibonnaci sequence
0th element -> 0
1st element -> 1
2nd element -> 1
3rd element -> 2
4th element -> 3
5th element -> 5
6th element -> 8

'''


def fib(n, dp):
    if n==0 or n==1:
        return n
    
    if dp[n]!=0:
        return dp[n]
    fib1=fib(n-1,dp)
    fib2=fib(n-2,dp)
    fibn=fib1+fib2
    dp[n]=fibn
    return fibn

def main():
    n = int(input())
    dp = [0] * (n + 1)
    print(fib(n, dp));

if __name__ == "__main__":
    main()