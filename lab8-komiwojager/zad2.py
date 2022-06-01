import networkx as nx
import matplotlib.pyplot as plt


import sys, pathlib
sys.path.append(pathlib.Path(__file__).parent)

from zad1 import path_len, load_cities, City

sys.path.insert(1, (pathlib.Path(__file__).parent.parent.parent / "wzmw-grpahs").absolute())
print(sys.path)
import graphlib as gl



def find_shortest_cycle(cities: list[City]) -> list[City]:
    ""
    #create_sectors()

class Graph(nx.Graph):

    def add_cities(self, cities: list[City]):
        for c in cities:
            self.add_node(c.id, pos=(c.x, c.y))
    
    def add_path(self, path: list[City]):
        prev = path[0]
        for c in path[1:]:
            self.add_edge([prev.id, c.id], prev.distance(c))
            prev = c


if __name__ == "__main__":
    G = Graph()
    gl.graphs.WeightedGraph
    cities = load_cities()
    G.add_cities(cities)
    G.add_path(cities + [cities[0]])
    nx.draw(G, pos={c.id: (c.x, c.y) for c in cities})
    plt.show()
