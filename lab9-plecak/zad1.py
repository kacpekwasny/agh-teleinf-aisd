from __future__ import annotations
from dataclasses import dataclass, field

"""
Fill the backpack with items starting from the bottom left corner, try recursively many combinations, but not all but only first hopefully best choices.

Create different item queues:
    by density = value/height/width - from highest to lowest density
    try to create a queue of same height items, that will fit the whole width.
    NO - the same for height - the backpack is a square, so that is unnecessary, it would result in two same solutions, one by height and one by width


"""

@dataclass
class Thing:
    id: int         # the id of the item
    width: int      # width
    height: int     # height
    value: int      # how important is this item
    
    # when the thing is placed in the backpack, here will be coordinates of the left bottom corner
    x: int = field(default=None)
    y: int = field(default=None)

    # whether the object was rotated by 90deg
    rotated: bool = field(default=False)

    # density - is calculated in post_init
    dens: float = field(default=None)

    def __post_init__(self):
        self.dens = self.value / self.width / self.height


    @property
    def w(self) -> int:
        return self.height if self.rotated else self.width 

    @property
    def h(self) -> int:
        return self.width if self.rotated else self.height 



def load_things(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        things: list[Thing] = []
        for l in f.read().splitlines()[2:]:
            if not l.strip():
                # is empty
                continue
            thing_data = list(map(int, l.split(",")))
            things.append(Thing(*thing_data))

    return things



class Backpack:

    def __init__(self, width, height) -> None:
        self.space = [[None for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

        # where are the place that the items could be placed
        self.start_places: list[tuple[int, int]] = [(0,0)]

        # sum of all placed items
        self.value = 0

        # ids of items in the backpack
        self.items: list[int] = []

    
    def place_item(self, x: int, y: int, item: Thing) -> bool:
        """
        params:
            x, y: int - the left bottom corner

        returns bool:
            True - successfully placed item there
            False - there is no place for this item
        """
        if item.id in self.items:
            return False

        # check if empty
        for row in self.space[y:y+item.h]:
            for field in row[x:x+item.w]:
                if field is not None:
                    return False

        # fill in the fields
        for row in self.space[y:y+item.h]:
            for i in range(x, x+item.w):
                row[i] = item.id
        item.x, item.y = x, y
        self.items.append(item.id)

        if (x, y) in self.start_places:
            self.start_places.remove((x, y))

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


    def remove_item(self, item: Thing) -> bool:
        "return False if no such item was found in backpack"
        if item.id not in self.items:
            return False
        for row in self.space[item.y:item.y+item.h]:
            for i in range(item.x, item.x+item.w):
                row[i] = None
        self.items.remove(item.id)
        item.x = item.y = None
        return True



def item_queue_desnsity(all_items: list[Thing]) -> list[Thing]:
    """
    return list of Things that contains only the items that are not in the backpack
    in the order that i think gives me the highest chance of finding a good solution
    of the backpack problem the fastest
    """
    return sorted(filter(
                        lambda thing: thing.x is None,
                        all_items),
                  key=lambda thing: thing.dens,
                  reverse=True)



def solve(backpack: Backpack, all_items: list[Thing]) -> Backpack:
    """
    recursively find the semi-best way to store items of the highest value.
    """

    #


def multiple_sort(things: list[Thing], *keys_reverse: tuple[function, bool]) -> list[Thing]:
    """
    sort things by one function, then all things that have the same parameter sort by second function and so on
    
    params:
        things: list of things to be sorted
        keys_reverse: tuples where [0] is a function that works as a key, and [1] is bool that says whether it should be a reversed sorted
    """
    # when there are no more functions to sort by return the list of things
    if len(keys_reverse)==0 or len(things)==1:
        return things
    print("things =\t", things)
    key, reverse = keys_reverse[0]
    keys_reverse = keys_reverse[1:]
    final_sorted = []
    things_sorted = sorted(things, key=key, reverse=reverse)
    print("things_sorted =\t", things_sorted)
    first_different_index = 0
    last_val = key(things_sorted[first_different_index])
    for i, thing in enumerate(things_sorted[1:], start=1):
        new_val = key(thing)
        if new_val != last_val:
            # section of items with the same value of key
            section = things_sorted[first_different_index:i]
            final_sorted += multiple_sort(section, *keys_reverse)
            first_different_index = i
            last_val = new_val
            print("in loop =\t", things_sorted)

    # the trailing items with the same value of key
    section = things[first_different_index:]
    final_sorted += multiple_sort(section, *keys_reverse)
    return final_sorted

ret = multiple_sort([[1, 10], [1, 2], [3, 10], [2, -1], [2, 1], [1, 10], [3, 9]],
                    (lambda x: x[0], False),
                    (lambda x: x[1], False)
                    )
print(ret)
for r in ret: print(id(r))



