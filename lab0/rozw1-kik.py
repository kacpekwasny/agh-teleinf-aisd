
from turtle import circle


def fmove(y, x):
    print("\033[%d;%dH" % (y, x))


class Kik:
    def __init__(self) -> None:
        self.board = [" " for _ in range(9)]
        self.circle_move = False

    """return None if no one won yet, or 'X' or 'O'"""
    def check_winner(self):
        p = self.board

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
        self.circle_move = not self.circle_move

    def run(self):
        won = None
        moves = 0
        while not won and moves <9:
            self.draw_board()
            self.make_move()
            won = self.check_winner()
            moves += 1
        self.draw_board()
        if won:
            print(f"{won} won!")
        else:
            print("Draw game")

        
if __name__ == "__main__":
    kik = Kik()
    kik.run()








