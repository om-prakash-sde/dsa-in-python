'''
1. You are given a number n, the size of a chess board.
2. You are required to place n number of queens in the n * n cells of board such that no 
queen can kill another.
Note - Queens kill at distance in all 8 directions
3. Complete the body of printNQueens function - without changing signature - to calculate 
and print all safe configurations of n-queens. Use sample input and output to get more idea.

Note -> The online judge can't force you to write the function recursively but that is what 
the spirit of question is. Write recursive and not iterative logic. 
The purpose of the question is to aid learning recursion and not test you.


'''



def isItasafeplaceForTheQueen(chess,row,col):
    for i in range(row-1,-1,-1):
        j=col
        if chess[i][j]==1:
            return False
    
    for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
            if chess[i][j]==1:
                return False
    
    for i,j in zip(range(row-1,-1,-1),range(col+1,len(chess))):
            if chess[i][j]==1:
                return False
    return True

def printNQueens(chess, qsf, row):
    if row == len(chess):
        print(qsf+".")
        return
    
    for col in range(0,len(chess)):
        if (isItasafeplaceForTheQueen(chess,row,col)) == True:
            chess[row][col] =1
            printNQueens(chess, qsf+str(row)+'-'+str(col)+", ",row+1)
            chess[row][col] = 0


def main():
    chess = [];
    n = int(input());
    for i in range(n) :
        a = []
        for j in range(n) :
            a.append(0);
        chess.append(a)
    printNQueens(chess, "", 0)

if __name__ == '__main__':
    main()