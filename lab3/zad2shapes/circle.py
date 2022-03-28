from dataclasses import dataclass, field
from math import pi


@dataclass(frozen=True)
class Circle:
    radius: float

    @property
    def area(self):
        return pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * pi * self.radius