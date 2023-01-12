"""
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are given a number x. 
4. You are required to find the first index at which x occurs in array a.
5. If x exists in array, print the first index where it is found
 otherwise print -1.

Note -> The online judge can't force you to write the function recursively
 but that is what the spirit of question is. Write recursive and not iterat
"""

# below method have logic to implement first index of an array
def Firstindex(arr, idx, x, n):
    # stopping the recursion at last index of array
    if idx==n:
        return -1
    # checking the condition with array at 0th position
    if arr[idx] == x:
        return idx
    # then implementing recursion in else condtion to check
    # left side array from 1 to nth position
    else:
        m=Firstindex(arr, idx+1,x,n)
        return m
    
# main method defined
def main():
    n = int(input())
    arr = []
    for i in range(n) :
        arr.append(int(input()))
    x = int(input())
    ans = Firstindex(arr, 0, x, n)
    print(ans)

# calling main method
if __name__ == "__main__":
    main()
    
#code by om prakash