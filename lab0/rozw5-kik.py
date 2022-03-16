
from tabnanny import check
from turtle import circle


def fmove(y, x):
    print("\033[%d;%dH" % (y, x))

def check_winner(p):
    for i in range(3):
        # poziomo
        if p[i*3]!=" " and p[i*3] == p[i*3+1] == p[i*3+2]:
            return p[i*3]

        # pionowo
        if p[i]!=" " and p[i] == p[3+i] == p[6+i]:
            return p[i]


    # ukośnie opadająco
    if p[0]!=" " and p[0]==p[4]==p[8]: return p[8]

    # ukośnie rosnąco
    if p[6]!=" " and p[6]==p[4]==p[2]: return p[2]
    
    return None


class Kik:
    def __init__(self) -> None:
        self.board = [" " for _ in range(9)]
        self.circle_move = False
        self.against_computer = True
        self.computer_char = "O"
        self.computer_move = False

    """return None if no one won yet, or 'X' or 'O'"""
    def check_winner(self):
        return check_winner(self.board)

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
        fmove(2,2)
        print(p)

    def make_move(self):
        move = "Circle's" if self.circle_move else "Cross's"
        correct_move = False
        while not correct_move:
            fmove(12, 0)
            mv = input(f"It is {move} turn, please pick: ")
            if mv.isdigit() and self.board[int(mv)]==" ":
                correct_move = True
            fmove(12, 0)
            print(" "*60)
        
        self.board[int(mv)] = "O" if self.circle_move else "X"

    def make_move_against_comp(self):
        move = "Circle's" if self.computer_char == "X" else "Cross's"
        correct_move = False
        while not correct_move:
            fmove(12, 0)
            mv = input(f"It is {move} turn, please pick: ")
            if mv.isdigit() and self.board[int(mv)]==" ":
                correct_move = True
            fmove(12, 0)
            print(" "*60)
        
        self.board[int(mv)] = "O" if self.computer_char=="X" else "X"

    def run(self):
        won = None
        moves = 0
        while not won and moves <9:
            self.draw_board()
            if self.computer_move:
                self.board[self.gen_move()] = self.computer_char
            else:
                if self.against_computer:
                    self.make_move_against_comp()
                else:
                    self.make_move()
            won = self.check_winner()
            moves += 1
            self.computer_move = not self.computer_move
            self.circle_move = not self.circle_move
        self.draw_board()
        if won:
            print(f"{won} won!")
        else:
            print("Draw game")

    """minmax algorithm to generate best move, returns index of field with highest chance of winning"""
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
        best_value = -999999
        best_index = values[0]
        for i, v in enumerate(values):
            if v == None:
                continue
            if v > best_value:
                best_index = i
                best_value = v
        return best_index


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
                if computer_move:
                    b[i] = comp_char
                    best_val = max(best_val, self.minmax(b, (not computer_move), comp_char, user_char))
                else:
                    b[i] = user_char
                    worst_val = min(worst_val, self.minmax(b, (not computer_move), comp_char, user_char))
                #best_val += self.minmax(b, not computer_move, comp_char, user_char)
        return best_val if computer_move else worst_val
        

        
if __name__ == "__main__":
    kik = Kik()
    kik.run()








