from cmath import sqrt
from dataclasses import dataclass

@dataclass(frozen=True)
class Triangle:
    points: tuple[tuple[float]]

    def __post_init__(self):
        if (len(self.points) != 3 or # if different number of points than 3
            any([len(t) != 2 for t in self.points])): # if point has different number of values than 2
            raise ValueError("points has to be a tuple ((x1, y1), (x2, y2), (x3, y3))")

    @property
    def area(self):
        p = self.points
        # area of triangle from matrix
        return 0.5 * abs( (p[1][0]-p[0][0]) * (p[2][1]-p[0][1]) - (p[1][1]-p[0][1]) * (p[2][0]-p[0][0]) )

    @property
    def perimeter(self):
        p = self.points
        # |AB| + |BC| + |CA|
        return (  sqrt((p[0][0] - p[1][0])**2 + (p[0][1] - p[1][1])**2) 
                + sqrt((p[1][0] - p[2][0])**2 + (p[1][1] - p[2][1])**2)
                + sqrt((p[2][0] - p[0][0])**2 + (p[2][1] - p[0][1])**2))

