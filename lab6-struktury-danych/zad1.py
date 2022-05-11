from __future__ import annotations

from dataclasses import dataclass, field


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
        sval = str("%.2f" % self.value).strip("0")
        if sval[-1] == ".":
            sval += "0"
        sval = "-" * level + sval
        indentation += len(sval)

        print(sval, sep="", end="")

        level += 1
        # print less tree
        if self.less:
            self.less.recursive_print(level, indentation)

        # print more tree
        if self.more:
            print(" " * (indentation * 1 if self.less else 0), end="")
            self.more.recursive_print(level, indentation)
        
        if not (self.less or self.more):
            print("")

    def search(self, value: float) -> bool:
        """
        returns: bool - Found True, not found False
        """
        if value == self.value:
            return True

        if value < self.value:
            if not self.less:
                return False
            return self.less.search(value)
        
        # value > self.value
        if not self.more:
            return False
        return self.more.search(value)

@dataclass
class Forest:
    trees: list[Tree] = field(init=False, default_factory=list)

    @staticmethod
    def root_val(val) -> float:
        return val//1 + 0.5

    def ins(self, value: float) -> Forest:
        if len(self.trees) == 0:
            self.trees.append(Tree(self.root_val(value)).ins(value))
            return self

        # does it go in the begging?
        if value < self.trees[0].value - 0.5:
            self.trees = [Tree(self.root_val(value)).ins(value)] + self.trees
            return self

        if self.trees[0].value - 0.5 <= value < self.trees[0].value + 0.5:
            self.trees[0].ins(value)
            return self

        # or is it the biggest number
        if value >= self.trees[-1].value + 0.5:
            self.trees.append(Tree(self.root_val(value)).ins(value))
            return self

        if self.trees[-1].value - 0.5 <= value < self.trees[-1].value + 0.5:
            self.trees[-1].ins(value)
            return self



        for i, t in enumerate(self.trees[1:-1], start=1):
            if t.value - 0.5 <= value < t.value + 0.5:
                t.ins(value)
                return self

            if self.trees[i-1].value + 0.5 <= value < self.trees[i+1].value-0.5:
                self.trees = self.trees[:i] + [Tree(self.root_val(value)).ins(value)] + self.trees[i:]
                return self

    def insert_multiple(self, *values) -> Forest:
        for v in values:
            self.ins(v)
        return self

    def print(self) -> None:
        for t in self.trees:
            t.recursive_print()

    def print_debug(self) -> None:
        for t in self.trees:
            print(t)

    def minimum(self, root_val: float) -> float:
        """
            raises:
                IndexError when there is no root with such value
        """
        mn = root_val
        t = [t for t in self.trees if t.value == root_val][0]
        while t.less:
            t = t.less
            mn = t.value
        return mn

    def maximum(self, root_val: float) -> float:
        """
            raises:
                IndexError when there is no root with such value
        """
        mn = root_val
        t = [t for t in self.trees if t.value == root_val][0]
        while t.more:
            t = t.more
            mn = t.value
        return mn

    def search(self, value: float) -> float:
        """
        returns: bool - Found True, not found False
        """
        for t in self.trees:
            if t.value - 0.5 <= value < t.value+0.5:
                return t.search(value)

        return False

if __name__ == "__main__":
    f = Forest()
    f.insert_multiple(1.5, 1.3, 1.6, 3.5, 3.7, 4.5, 4.0, 4.99, 7.5, 7.3, 7.8, 7.7, 7.6, 7.9, 9.5, 9.3)
    # t = Tree(3)
    # t.ins(1).ins(2).ins(3).ins(4).ins(5).ins(0.5)
    # t.recursive_print()
    # f.print_debug()
    f.print()
    print(f.minimum(7.5))
    print(f.maximum(7.5))