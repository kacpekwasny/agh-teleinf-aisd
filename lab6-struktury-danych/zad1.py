from __future__ import annotations

from dataclasses import dataclass, field
from list

@dataclass
class NumForest:
    pass


@dataclass
class Tree:
    value: float
    less: Tree = field(init=False, default=None)
    more: Tree = field(init=False, default=None)

    def ins(self, value: float) -> Tree:
        """insert value in to the tree struct"""
        if value > self.value:
            if self.more is not None:
                self.more.ins(value)
                return self
            self.more = Tree(value)
            return self

        if value < self.value:
            if self.less is not None:
                self.less.ins(value)
                return self
            self.less = Tree(value)
            return self

        # the value == self.value... So just leave it?
        return self


    def recursive_print(self, level=0, indentation=0) -> None:
        sval = str("%.2f" % self.value)
        sval = "-" * level + sval
        indentation += len(sval)

        print(sval, sep="", end="")

        level += 1
        # print less tree
        if self.less:
            self.less.recursive_print(level, indentation)

        # print more tree
        if self.more:
            print("\n" + " " * indentation, end="")
            self.more.recursive_print(level, indentation)


@dataclass
class Forest:
    trees: list[Tree] = field(init=False, default_factory=list)


    def ins(self, value: float) -> Forest:
        if len(self.trees) == 0:
            self.trees.append(Tree(value))
            return

        # does it go in the begging?


        # or is it the biggest number
        if value > 


        for i, t in enumerate(self.trees[1:-1], start=1, ):
            if t.value - 0.5 <= value < t.value + 0.5:
                t.ins(value)
                return

            if






if __name__ == "__main__":
    t = Tree(3)
    t.ins(1).ins(2).ins(3).ins(4).ins(5).ins(0.5)
    t.recursive_print()
    x = Forest()
    print(x)
    print(x.trees)