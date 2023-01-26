"""
Print Encodings
===============
1. You are given a string str of digits. (will never start with a 0)
2. You are required to encode the str as per following rules
    1 -> a
    2 -> b
    3 -> c
    ..
    25 -> y
    26 -> z
3. Complete the body of printEncodings function - without changing signature - to calculate and print all encodings of str.
Use the input-output below to get more understanding on what is required
123 -> abc, aw, lc
993 -> iic
013 -> Invalid input. A string starting with 0 will not be passed.
103 -> jc
303 -> No output possible. But such a string maybe passed. In this case print nothing.

Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.

"""



import sys
sys.setrecursionlimit(10000)

def printEncodings(ques,asf):
    if len(ques)==0:
        print(asf)
        return
    elif len(ques) ==1:
        ch=ques[0]
        if ch == '0':
            return
        else:
            chv = int(ch)
            code=chr(ord("a")+(chv-1))
            asf=asf+code
            print(asf)
    else:
        ch=ques[0]
        roq=ques[1:]
        if ch == '0':
            return
        else:
            chv = int(ch)
            code=chr(ord("a")+(chv-1))
            printEncodings(roq,asf+code)
        
        ch12 = ques[0:2]
        roq1 = ques[2:]
        
        ch12v=int(ch12)
        if ch12v<=26:
            code=chr(ord("a")+(ch12v-1))
            printEncodings(roq1,asf+code)
            

def main():
    s=input()
    s=s.strip()
    printEncodings(s,"")

if __name__ =='__main__':
    main()