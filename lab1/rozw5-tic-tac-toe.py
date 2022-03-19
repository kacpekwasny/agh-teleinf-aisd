#
# Kacper Kwasny 16.03.2022
# rozw5-tic-tac-toe.py
#

from random import choice
from sys import argv, stdout


"""
Move terminal cursor around.
This function is mostly used to overwrite the displayed board
"""
def fmove(y, x):
    print("\033[%d;%dH" % (y, x))


"""
Take in List of len = 9 that represents a tic tac toe board and check if someone won,
items in the list may be "X", "O" or " "
If X won return "X"
If O won return "O"
If no one won return None - this might be beacuse the game was Draw or beacuse it has not ended yet
"""
def check_winner(p):
    for i in range(3):
        # check horizontal
        if p[i*3]!=" " and p[i*3] == p[i*3+1] == p[i*3+2]:
            return p[i*3]

        # check vertical
        if p[i]!=" " and p[i] == p[3+i] == p[6+i]:
            return p[i]


    # obliquely falling
    if p[0]!=" " and p[0]==p[4]==p[8]: return p[8]

    # obliquely raising
    if p[6]!=" " and p[6]==p[4]==p[2]: return p[2]
    
    return None

"""overwrite begging of terminal with spaces"""
def clear_terminal():
    fmove(0,0)
    print( (" "*200+"\n") * 30 )
    fmove(0,0)

class TicTacToe:
    def __init__(self, circle_move_first: bool, against_computer: bool, computer_char_X: bool, computer_move_first: bool, visualize_minmax: bool) -> None:
        self.board = [" " for _ in range(9)]
        self.circle_move = circle_move_first                    # Chose if Cross or circle is first
        self.against_computer = against_computer                # False -> You will play user vs user, True -> You play vs computer
        
        self.computer_char = "X" if computer_char_X else "O"    # Chose which charachter will computer use, you will use the opposite one
        self.computer_char_X = computer_char_X
        
        self.computer_move = computer_move_first                # False -> The user has first move
        self.computer_move_first = computer_move_first

        self.visualize_minmax = visualize_minmax                # True -> print a parralel board that shows which fields have which value calculated by minmax


    """return None if no one won yet, or 'X' or 'O'"""
    def check_winner(self):
        return check_winner(self.board)

    """Overwrite previous tic tac toe board"""
    def draw_board(self):
        p = self.board
        p = f"""-------------
| {p[0]} | {p[1]} | {p[2]} |
-------------
| {p[3]} | {p[4]} | {p[5]} |
-------------
| {p[6]} | {p[7]} | {p[8]} |
-------------
"""
        # move the start of print to make it look a bit nicer
        fmove(0,0)
        print(p)

    def draw_board_and_minmax_out(self, board_before_move, minmax_out):
        p = self.board
        board = f"""-------------
| {p[0]} | {p[1]} | {p[2]} |
-------------
| {p[3]} | {p[4]} | {p[5]} |
-------------
| {p[6]} | {p[7]} | {p[8]} |
-------------
"""
        o = []
        for f, v in zip(board_before_move, minmax_out):
            o.append((f"\b{v}" if v < 0 else v) if f == " " else f)            

        out = f"""-------------
| {o[0]} | {o[1]} | {o[2]} |
-------------
| {o[3]} | {o[4]} | {o[5]} |
-------------
| {o[6]} | {o[7]} | {o[8]} |
-------------
"""
        for_print = ""
        for l1, l2 in zip(board.splitlines(), out.splitlines()):
            for_print += l1 + "\t\t" + l2 + "\n"

        fmove(0,0)
        print(for_print)

    """Take input from user as [1-9], if input is invalid display error message and take input again until is valid.
    This method is prepared for PvP"""
    def make_move(self):
        invalid_msg_line_no = 14
        input_line_no = 12
        if self.against_computer:
            move = "Circle's" if self.computer_char == "X" else "Cross's"
        else:
            move = "Circle's" if self.circle_move else "Cross's"
    
        correct_move = False
        while not correct_move:
            invalid_msg = "Invalid input! Please input digit from 1 to 9 or type in exit or reset."
            fmove(input_line_no, 0)
            mv = input(f"It is {move} turn, please pick: ")
            if mv.lower() in ["exit", "e"]:
                fmove(0,0)
                clear_terminal()
                exit()
            
            if  mv.lower() in ["reset", "r"]:
                fmove(0,0)
                clear_terminal()
                self.__init__(self.circle_move, self.against_computer, self.computer_char_X, self.computer_move_first, self.visualize_minmax)
                self.run()
                exit()

            if mv.isdigit() and self.board[int(mv)-1]==" ":
                correct_move = True
            else:
                fmove(invalid_msg_line_no, 0)
                print(invalid_msg)

            # overwrite line that took input
            fmove(input_line_no, 0)
            print(" "*60)

        # overwrite invalid_msg with spaces
        fmove(invalid_msg_line_no, 0)
        print(" "*len(invalid_msg))
        
        # input is valid, so the board is filled with appropriate value'
        if self.against_computer:
            self.board[int(mv)-1] = "O" if self.computer_char=="X" else "X"
        else:
            self.board[int(mv)-1] = "O" if self.circle_move else "X"

    """Generate best field to place next move. The function uses minmax algorithm to generate best move, returns index of field with highest chance of winning"""
    def gen_move(self):
        # It is computers move!
        # assuming the game has not ended
        comp, user = (("O", "X") if self.computer_char == "O" else ("X", "O"))
        values = [(0 if f == " " else None) for f in self.board]
        for i, f in enumerate(self.board):
            if f == " ":
                b = self.board[:]
                b[i] = comp
                values[i] = self.minmax(b, False, comp, user)
        self.minmax_values = values[:]
        best_value = -99999
        best_val_dict = {}
        best_index = {} # Whatever, even if there is a None under this index, there will be found an index with a higher value than -9999
        for i, v in enumerate(values):
            if v == None:
                continue
            if v > best_value:
                best_val_dict[v] = [i]
                best_value = v
            elif v == best_value:
                best_val_dict[v].append(i)

        return choice(best_val_dict[best_value])

    def minmax(self, board, computer_move, comp_char, user_char):
        w = check_winner(board)
        # if computer won
        if w == comp_char:
            return 1
        # if user won
        if w == user_char:
            return -1
        # if the game was draw
        if " " not in board and w==None:
            return 0

        best_val = -1
        worst_val = 1
        # the game has not ended
        for i, f in enumerate(board):
            if f == " ":
                b = board[:]
                
                # if it is computers move return the best possible move 
                if computer_move:
                    b[i] = comp_char
                    best_val = max(best_val, self.minmax(b, (not computer_move), comp_char, user_char))
                
                # if this is users move assume the user will make his best possible move
                else:
                    b[i] = user_char
                    worst_val = min(worst_val, self.minmax(b, (not computer_move), comp_char, user_char))
        return best_val if computer_move else worst_val

    """Start the game with settings that were passed during the initialization of TicTacToe(...)"""
    def run(self):
        clear_terminal()
        won = None
        moves = 0 

        # If someone won, or there were 9 moves
        while not won and moves <9:
            moves += 1

            # draw board or draw board with minmax visualization
            if self.visualize_minmax and hasattr(self, "minmax_values"):
                self.draw_board_and_minmax_out(board_before_move, self.minmax_values)
                delattr(self, "minmax_values")
            else:
                self.draw_board()

            # make a move
            if self.against_computer and self.computer_move:
                board_before_move = self.board[:]
                self.board[self.gen_move()] = self.computer_char
            else:
                self.make_move()

            # Because one cannot win in less than 5 moves
            if moves >= 5:
                won = self.check_winner()
            
            self.computer_move = not self.computer_move
            self.circle_move = not self.circle_move
            clear_terminal()

        # Draw the board after the last move
        if self.visualize_minmax and hasattr(self, "minmax_values"):
            self.draw_board_and_minmax_out(board_before_move, self.minmax_values)
        else:
            self.draw_board()
        
        # Information about the game end status
        if won:
            print(f"{won} won!")
        else:
            print("Draw game")


        
if __name__ == "__main__":
    # Circle move first,    against computer,   computer has X,    computer has first turn
    circle_move_first = False
    against_comp = True
    computer_has_X = True
    computer_has_first_turn = False
    visualize_minmax = False

    # check if help was asked for
    for h in ["h", "/h", "-h", "--h", "help", "/help", "-help", "--help", "?", "/?", "-?", "--?"]:
        if h in argv:
            print("""
run with no args for a game against computer

    -o      circle will have the first turn (only makes difference in PvP mode)
    -pvp    player vs player, no computer

    -x      computer is playing the 'X', you will be playing the 'O'
    -comp   computer will have the first turn
    -v      visualize minmax

    "h", "/h", "-h", "--h", "help", "/help", "-help", "--help", "?", "/?", "-?", "--?"
            to display help
""")
            exit()

    circle_move_first = (not circle_move_first) if "-o" in argv else circle_move_first
    against_comp = (not against_comp) if "-pvp" in argv else against_comp
    computer_has_X = (not computer_has_X) if "-x" in argv else computer_has_X
    computer_has_first_turn = (not computer_has_first_turn) if "-comp" in argv else computer_has_first_turn
    visualize_minmax = (not visualize_minmax) if "-v" in argv else visualize_minmax


    ttt = TicTacToe(circle_move_first, against_comp, computer_has_X, computer_has_first_turn, visualize_minmax)
    ttt.run()
