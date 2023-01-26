"""
1. You are given a string str.
2. Complete the body of printPermutations function - without changing signature - to 
calculate and print all permutations of str.
Use sample input and output to take idea about permutations.

Note -> The online judge can't force you to write the function recursively but that is
 what the spirit of question is. Write recursive 
and not iterative logic. The purpose of the question is to aid learning recursion
 and not test you.

"""

def printPermutations(s,asf):
    if len(s)==0:
        print(asf)
        return
    for i in range(0,len(s)):
        ch=s[i]
        rosl=s[0:i]
        rosr=s[i+1:]
        qos=rosl+rosr
        printPermutations(qos,asf+ch)
    

def main():
    s=input()
    s=s.strip()  # in pepcoding editor not running without strip
    printPermutations(s,'')


if __name__ == '__main__':
    main()