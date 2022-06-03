from __future__ import annotations
from dataclasses import dataclass, field
from random import randint
import sys
import pygame
from pygame.locals import *

"""
Fill the backpack with items starting from the bottom left corner, try recursively many combinations, but not all but only first hopefully best choices.

Create different item queues:
    by density = value/height/width - from highest to lowest density
    try to create a queue of same height items, that will fit the whole width.
    NO - the same for height - the backpack is a square, so that is unnecessary, it would result in two same solutions, one by height and one by width


"""

@dataclass
class Item:
    id: int         # the id of the item
    _width: int      # width
    _height: int     # height
    value: int      # how important is this item
    
    # when the thing is placed in the backpack, here will be coordinates of the left bottom corner
    x: int = field(default=None)
    y: int = field(default=None)

    # whether the object was rotated by 90deg
    rotated: bool = field(default=False)

    # density - is calculated in post_init
    dens: float = field(default=None)

    def __post_init__(self):
        self.dens = self.value / self._width / self._height
        if self._width < self._height:
            self.rotated = True


    @property
    def w(self) -> int:
        return self._height if self.rotated else self._width 

    @property
    def h(self) -> int:
        return self._width if self.rotated else self._height 

@dataclass
class StartPlace:
    """
    stores information on the start place, where an item could be placed
    """
    x: int
    y: int

    space_x: int
    "how much space is to right, until the right wall or the end of item below"
    space_y: int


def load_items(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        things: list[Item] = []
        for l in f.read().splitlines()[2:]:
            if not l.strip():
                # is empty
                continue
            thing_data = list(map(int, l.split(",")))
            things.append(Item(*thing_data))

    return things



def randcol() -> tuple[int, int, int]:
    return (
        randint(10, 150),
        randint(10, 150),
        randint(10, 150)
    )

class Backpack:

    def __init__(self, width, height) -> None:
        self.space = [[None for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        self.available_space = width * height

        # where are the place that the items could be placed
        self.start_places: list[StartPlace] = [StartPlace(0, 0, width, height)]

        # sum of all placed items
        self.value = 0

        # ids of items in the backpack
        self.items: list[int] = []
        self.real_items: list[Item] = []


    def check_space_is_free(self, x: int, y: int, W: int, H: int) -> tuple[bool, tuple[int, int]]:
        """
        check if space W x H in the coords (x, y) is empty
        returns:
            (
                is_free: bool,
                coords: int, int    # where is a not empty field
            )
        """
        for yy, row in enumerate(self.space[y:y+H], start=y):
            for xx, field in enumerate(row[x:x+W], start=x):
                if not field is None:
                    return False, (xx, yy)

        return True, None


    def add_start_place(self, x: int, y: int) -> bool:
        """return StartPlace(x,y,w,h) that has been created, for the x and y"""
        for xx in range(x, self.width):
            if not self.space[y][xx] is None:
                xx -= 1
                break
        
        for yy in range(y, self.height):
            if not self.space[yy][x] is None:
                yy -= 1
                break
        
        sp = StartPlace(x, y, xx-x+1, yy-y+1)
        self.start_places.append(sp)
        return sp


    def remove_start_place(self, sp: StartPlace) -> bool:
        "return False if no starting place was removed. True if a place was removed."
        if sp in self.start_places:
            self.start_places.remove(sp)
            return True
        return False


    def fill_space(self, x: int, y: int, item: Item):
        # fill in the fields
        for row in self.space[y:y+item.h]:
            for i in range(x, x+item.w):
                row[i] = item.id
        

    def put_item(self, x: int, y: int, item: Item):
        """
        Does not check anything, assumes it has been done
        subtract from self.available_space
        params:
            x, y: int - the left bottom corner
        """
        self.fill_space(x, y, item)
        item.x, item.y = x, y
        self.items.append(item.id)
        self.real_items.append(item)
        self.available_space -= item._height * item._width


    def try_put_item_in_place(self, p: StartPlace, i: Item) -> bool:
        """
        return success if there was space for that Item
        """
        
        # check if there is free space
        isfree, coords = self.check_space_is_free(p.x, p.y, i.w, i.h)
        if not isfree:
            # do something
            p.space_x = coords[0] - p.x
            p.space_y = coords[1] - p.y
            
            return False
        
        self.put_item(p.x, p.y, i)
        return True



        if p in self.start_places:
            self.start_places.remove(p)

        place = (x + item.w, y)
        # accept this place only if it is at the bottom, or on top of another object
        # and isn't outside the backpacks space
        if (self.width < x + item.w -1 and              # is not outside
           (y == 0 or                                   # is at the bottom of backpack
           self.space[y-1][x + item.w] is not None)):   # is not in the air (do not waste space, place item at the lowest point)
            
            self.start_places.append(place)

        place = (x, y + item.h)
        # accept this place only if it isn't outside the backpacks space (because it most certainly is on top of an item)
        if y + item.h < self.height - 1:
            self

        return True


    def print(self):
        print("#"*(2*self.width + 3))
        for row in self.space[::-1]:
            print("# ", end="")
            for field in row:
                print(("_ " if field is None else f"{field} ").ljust(3), end="")
            print("#")
        print("#"*(2*self.width+3))

    def draw(self):
        
        SCALE = 1080//(self.height + 10)
        WIDTH = self.width * SCALE
        HEIGHT = self.height * SCALE
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

        for item in self.real_items:
            itemW = item.w * SCALE
            itemH = item.h * SCALE
            pygame.draw.rect(DISPLAYSURF, randcol(), pygame.Rect(item.x * SCALE,
                                                                 item.y * SCALE,
                                                                 itemW,
                                                                 itemH))

        for sp in self.start_places:
            pygame.draw.rect(DISPLAYSURF, (255, 0, 0), pygame.Rect(sp.x * SCALE,
                                                                 sp.y * SCALE,
                                                                 SCALE//4,
                                                                 SCALE//4))

        while True: # main game loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            pygame.display.update()

    def get_value(self) -> int:
        return sum([i.value for i in self.real_items])



def items_queue(items: list[Item]) -> list[Item]:
    """
    list of things, that are sorted from lowest to highest density.
    I am not doing reverse, because I want to use .pop(), and .pop(0) takes longer
    """
    return sorted(items, key=lambda thing: thing.dens, reverse=True)


def solve(backpack: Backpack, items: list[Item]) -> Backpack:
    """
    naive algorithm
    find the semi-best way to store items of the highest value.
    """

    placed_item = True
    while placed_item:
        # when the next iteration of loop starts, but the internal part of loop haven't managed to place a new item
        # the `placed_item` will still be False, and thus the loop ends - the backpack is full.
        placed_item = False

        items = items_queue(items)
        for item in items:
            # find starting place
            for p in backpack.start_places:
                for _ in [1, 2]:
                    # this loop is just to rotate the item
                    if p.space_x >= item.w and p.space_y >= item.h:
                        ok = backpack.try_put_item_in_place(p, item)
                        if ok:
                            placed_item = True
                            # remove placed item
                            items.remove(item)

                            # remove used StartPlace
                            backpack.remove_start_place(p)
                            
                            # add new start places
                            if p.x + item.w < backpack.width:
                                backpack.add_start_place(p.x + item.w, p.y)
                            if p.y + item.h < backpack.height:
                                backpack.add_start_place(p.x, p.y+item.h)
                            if p.x + item.w < backpack.width and p.y + item.h < backpack.height:
                                backpack.add_start_place(p.x + item.w, p.y + item.h)

                            backpack.start_places.sort(key=lambda sp: sp.x + sp.y )

                            backpack.draw()
                            break
                    item.rotated = not item.rotated
            
                if placed_item:
                    break

            if placed_item:
                break


if __name__ == "__main__":
    FILE_PATH = "C:\\Users\\quatr\\IT\\Code\\agh-teleinf-aisd\\lab9-plecak\\packages20.txt"
    FILE_PATH = sys.argv[1]
    
    SIZE = 20
    SIZE = int(sys.argv[2])

    b = Backpack(SIZE, SIZE)
    
    solve(b, load_items(FILE_PATH))
    b.draw()
    print(b.get_value())
 


def not_placed_items(): pass

def build_bottom(b: Backpack, items: Item):
    """
    find the best item to be placed at the bottom of the backpack
    if there is no ideal item, return None
    An item is considered ideal when can be placed flush with the item on left and thus making a level plane on the floor of backpack 
    """
    pass

def build_left(b: Backpack, items: Item):
    """
    find the best item to be placed at the left of the backpack
    if there is no ideal item, return None
    An item is considered ideal when can be placed flush with the item on underneath and thus moving the left wall to right,
    not necesiraly the whole wall
    """
    pass
