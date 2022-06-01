from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

DIR_LAB8 = Path(__file__).parent
CITIES_FILE = (DIR_LAB8 / "TSP.txt").resolve()


@dataclass
class City:
    id: int
    x: float
    y: float

    def distance(self, other: City) -> float:
        return ( (self.x - other.x)**2 + (self.y - other.y)**2 ) ** .5


def load_cities():
    with open(CITIES_FILE, "r", encoding="utf-8") as f:
        cities: list[City] = []
        for l in f.read().splitlines():
            city_data = list(map(float, l.split("\t")))
            cities.append(City(
                    int(city_data[0]),
                    *city_data[1:]
                ))

    return cities

def path_len(cities: list[City]) -> float:
    "length of the path between cities in the specified order"
    path = 0
    prev = cities[0]
    for c in cities[1:]:
        path += prev.distance(c)
        prev = c
    return path  


if __name__ == "__main__":
    cs = load_cities()
    print( path_len(cs + [cs[0]]))
        
