      

class Hanoi:
    tower: list[int]
    print = True    
    def gen_tower(self, tower_height):
        """
        returns:
            [
                [tower_height ... 2, 1],
                [],
                []
            ]
        """
        if tower_height < 1: raise ValueError("tower_height argument has to be at least 1")
        self.tower = [list(range(1, tower_height+1))[::-1], [], []]


    def make_legal_move(self, pole1: list[int], pole2: list[int], name1: str, name2: str):
        if not len(pole1):
            pole1.append(pole2.pop())
            #if self.print: self.announce_move(name2, name1, pole1[-1], pole2, pole1)
            return
        
        if not len(pole2):
            pole2.append(pole1.pop())
            #if self.print: self.announce_move(name1, name2, pole2[-1], pole1, pole2)
            return
        
        if pole1[-1] < pole2[-1]:
            pole2.append(pole1.pop())
            #if self.print: self.announce_move(name1, name2, pole2[-1], pole1, pole2)
            return
        
        if pole1[-1] > pole2[-1]:
            pole1.append(pole2.pop())
            #if self.print: self.announce_move(name2, name1, pole1[-1], pole2, pole1)
            return
        
    @staticmethod
    def announce_move(sour: str, dest: str, val: str, pole_sour, pole_dest) -> None:
        # print announcement of executed move
        print(f"{sour} -> {val} -> {dest}")


    def solve(self):
        n = 2 ** len(self.tower[0]) - 1

        s, d, b = "Sour", "Dest", "Buff"
        # switch destination, and buffer according to the algorithm
        if len(self.tower[0]) % 2 == 0:
            d, b = b, d

        #while len(self.tower[0]) or len(self.tower[2]):
        for _ in range(1, n+1, 3):
            print(self.tower)
            self.make_legal_move(self.tower[0], self.tower[1], s, d)
            self.make_legal_move(self.tower[0], self.tower[2], s, b)
            self.make_legal_move(self.tower[1], self.tower[2], d, b)

        print(self.tower)

if __name__ == "__main__":
    h = Hanoi()
    h.gen_tower(6)
    h.solve()





