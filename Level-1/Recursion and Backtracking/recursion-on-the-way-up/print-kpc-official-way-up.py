"""
Print-kpc
=========
1. You are given a string str. The string str will contains numbers only, 
where each number stands for a key pressed on a mobile phone.
2. The following list is the key to characters map
    0 -> .;
   1 -> abc
   2 -> def
   3 -> ghi
   4 -> jkl
   5 -> mno
   6 -> pqrs
   7 -> tu
   8 -> vwx
   9 -> yz
3. Complete the body of printKPC function
 - without changing signature - to print the list of all words that 
 could be produced by the keys in str.
Use sample input and output to take idea about output.


"""

import sys
sys.setrecursionlimit(10000)

codes=[".;","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"]
def print_kpc(ques,ans):
    if len(ques)==0: \\ in some compiler it will run 1 in place of 0 as object in python exclude last value in string
        print(ans)
        return
    ch=ques[0]
    roq=ques[1:]
    codeforch=codes[int(ch)]
    for i in range(0,len(codeforch)):
        cho=codeforch[i]
        print_kpc(roq,ans+cho)
   
   
def main():
    s=input()
    print_kpc(s,"")

if __name__ == '__main__':
    main()