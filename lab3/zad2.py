from zad2shapes import Circle, Triangle, Square

def main():
    ci = Circle(radius=2)
    tr = Triangle(points=(
        (0, 0),
        (2, 0),
        (0, 2)
    ))
    sq = Square(side=2)
    figures = [ci, tr, sq]
    for f in figures:
        print("\n")
        print(f)
        print(f"{f.__class__.__name__}: area={f.area}, perimeter={f.perimeter}")

if __name__ == "__main__":
    main()