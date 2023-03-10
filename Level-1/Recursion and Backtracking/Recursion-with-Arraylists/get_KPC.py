'''1. You are given a string str. The string str will contains numbers only, where each number stands for a key pressed on a mobile phone.
2. The following list is the key to characters map :
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
3. Complete the body of getKPC function - without changing signature - to get the list of all
 words that could be produced by the keys in str.
Use sample input and output to take idea about output.

Note -> The online judge can't force you to write the function recursively but that is what
 the spirit of question is. Write recursive and not iterative logic. 
 The purpose of the question is to aid learning recursion and not test you.'''




codes=['.;','abc','def','ghi','jkl','mno','pqrs','tu','vwx','yz']
def getKPC(s):
    if len(s)==0:
        return ['']
    ch=s[0]
    ros=s[1:]
    rres=getKPC(ros)
    mres=[]
    codeforch=codes[int(ch)]
    for i in range(0,len(codeforch)):
        chcode=codeforch[i]
        for rstr in rres:
            mres.append(chcode+rstr)
    return mres
            
        
    
    

def main():
    s = input()
    ans = getKPC(s)
    print("[" + ', '.join(ans) + "]")
    
main()