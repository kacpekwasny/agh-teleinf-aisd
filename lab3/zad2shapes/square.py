from dataclasses import dataclass

@dataclass(frozen=True)
class Square:
    side: float

    def __post_init__(self):
        if not self.side > 0:
            raise ValueError("squares side has to be > 0")
    
    @property
    def area(self):
        return self.side**2

    @property
    def perimeter(self):
        return self.side * 4
