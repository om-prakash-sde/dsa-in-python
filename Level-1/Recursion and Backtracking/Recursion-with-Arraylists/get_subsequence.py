#get subsequence using recursion
'''
1. You are given a string str.
2. Complete the body of getSS function - without changing signature - to calculate all subsequences of str.
Use sample input and output to take idea about subsequences.

Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is.
Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.

'''
def getSS(s):
    if len(s)==0:
        return [""]
    ch=s[0]
    ros=s[1:]
    rres=getSS(ros)
    mres=[]
    for i in rres:
        mres.append(i)
    for i in rres:
        mres.append(ch+i)
    return mres
    
    
def main():
    s = input()
    ans = getSS(s)
    print("[" + ', '.join(ans) + "]")
    
main()