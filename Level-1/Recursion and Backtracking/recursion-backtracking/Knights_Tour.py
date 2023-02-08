"""
Knights Tour
===========
1. You are given a number n, the size of a chess board.
2. You are given a row and a column, as a starting point for a knight piece.
3. You are required to generate the all moves of a knight starting in (row, col)
 such that knight visits all cells of the board exactly once.
4. Complete the body of printKnightsTour function - without changing signature - to calculate
 and print all configurations of the chess board representing the route of knight through 
 the chess board. Use sample input and output to get more idea.
 
Note -> When moving from (r, c) to the possible 8 options give first precedence to 
(r - 2, c + 1) and move in clockwise manner to explore other options.
Note -> The online judge can't force you to write the function recursively but that
is what the spirit of question is. Write recursive and not iterative logic. The 
purpose of the question is to aid learning recursion and not test you.

"""

def displayBoard(chess):
    for i in range(len(chess)) :
        for j in range(len(chess)) :
            print(chess[i][j], "", end = '');
        print()
    print()


def printKnightsTour(chess, n, r, c, upcomingMove):
    # write your code here
    if r<0 or c<0 or r>=len(chess) or c>=len(chess) or chess[r][c] > 0:
        return
    elif upcomingMove==(n*n):
        chess[r][c]=upcomingMove
        displayBoard(chess)
        chess[r][c]=0
        return
    
    chess[r][c]=upcomingMove
    printKnightsTour(chess,n,r-2,c+1,upcomingMove+1)
    printKnightsTour(chess,n,r-1,c+2,upcomingMove+1)
    printKnightsTour(chess,n,r+1,c+2,upcomingMove+1)
    printKnightsTour(chess,n,r+2,c+1,upcomingMove+1)
    printKnightsTour(chess,n,r+2,c-1,upcomingMove+1)
    printKnightsTour(chess,n,r+1,c-2,upcomingMove+1)
    printKnightsTour(chess,n,r-1,c-2,upcomingMove+1)
    printKnightsTour(chess,n,r-2,c-1,upcomingMove+1)
    chess[r][c]=0
    



def main():
    n = int(input());
    chess = [];
    for i in range(n) :
        a = [];
        for j in range(n) :
            a.append(0);
        chess.append(a);
    row = int(input());
    col = int(input());
    printKnightsTour(chess, n, row, col, 1);

if __name__ == '__main__':
    main()