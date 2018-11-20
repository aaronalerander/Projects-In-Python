chessboard = [ ['wr', 'wb', 'wn', 'wk', 'wq', 'wn', 'wb', 'wr'],
               ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
               ['--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--'],
               ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
               ['br', 'bb', 'bn', 'bk', 'bq', 'bn', 'bb', 'br'] ]


def print_board_state(board):
    row_board = len(board)
    coloumn_board = len(board[0])
    for row in range(row_board):
        for coloumn in range(coloumn_board):
            print(board[row][coloumn]," ",end="")
        print()


#ask about inputing tuple

def is_space_occupied(player,board,x,y):
    
    if player == ('w'):
        if "b" in board[x][y]:
            print("occupied by other player")
        elif "w" in board[x][y]:
            print("your own peice is there")
        else:
            print("ok")
        
        
    else:
        if "w" in board[x][y]:
            print("occupied by other player")
        elif "b" in board[x][y]:
            print("your own peice is there")
        else:
            print("ok")
            


def is_valid_move(player,board,piece,first_x,first_y,sec_x,sec_y):
    if player == ('w'):
        if piece == ('n'):
            if first_x != 3 or 6 and first_y != 1:
                print("That is not a knight")
            else:
            

                if sec_x == first_x + 1 or first_x -1 and sec_y == + 2:
                    print("valid with knight")
                    if is_space_occupied(player,chessboard,sec_x,sec_y) == ("ok") or ("occupied by other player"):
                        print("piece is moved")
                    else:
                        print("sorry dude, couldnt move ther")
                    
                else:
                    print("not valid with knight")
        else:
            if first_y != 2:
                print("not a pawn")
            else:
                if sec_y == first_y + 1: 
                    print("valid with pawn")
                    if is_space_occupied(player,chessboard,sec_x,sec_y) == ("ok"):
                        print("pawn piece is moved")

                    else:
                        print("sorry dude, couldnt move pawn ther")
                else:
                    print("can't move pawn like that")
                    
              
    else:
        if piece == ('n'):
            if first_x != 3 or 6 and first_y != 8:
                print("That is not a rook")
            else:
            

                if sec_x == first_x + 1 or first_x -1 and sec_y == first_y - 2 or first_y + 2:
                    print("valid with knight")
                    if is_space_occupied(player,chessboard,sec_x,sec_y) == ("ok") or ("occupied by other player"):
                        print("piece is moved")
                    else:
                        print("sorry dude, couldnt move ther")
                    
                else:
                    print("not valid with knight")
        else:
            if first_y != 7:
                print("not a pawn")
            else:
                if sec_y == first_y - 1:
                    print("valid with pawn")
                    if is_space_occupied(player,chessboard,sec_x,sec_y) == ("ok"):
                        print("pawn piece is moved")
                    else:
                        print("sorry dude, couldnt move ther")
                else:
                    print("not valid with pawn")

                    
print_board_state(chessboard)  
print()
is_space_occupied("b",chessboard,1,1)
print()
is_valid_move("w",chessboard,"n",3,1,5,7)
is_valid_move("w",chessboard,"p",2,2,2,1)
    
    