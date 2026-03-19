import math
from enum import Enum


class Vector2:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def normalize(self) -> None:

        length = self.length()

        if length != 0:
            self.x /= length
            self.y /= length

    def normalized(self) -> "Vector2":

        length = self.length()

        if length == 0:
            return Vector2.zero()

        return Vector2(
            self.x / length,
            self.y / length
        )

    def perpendicular(self, opposite=False) -> "Vector2":
        return Vector2(-self.y, self.x) if not opposite else Vector2(self.y, -self.x)

    def distance_to(self, other: "Vector2") -> "Vector2":
        return Vector2(other.x - self.x, other.y - self.y)

    @staticmethod
    def dot(v1: "Vector2", v2: "Vector2") -> float:
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def distance(v1: "Vector2", v2: "Vector2") -> "Vector2":
        return Vector2(v2.x - v1.x, v2.y - v1.y)

    @staticmethod
    def zero() -> "Vector2":
        return Vector2(0, 0)

    @staticmethod
    def from_dir(direction: "Direction") -> "Vector2":
        return Vector2(*direction.value)

    def __add__(self, other):

        if not isinstance(other, Vector2):
            return NotImplemented

        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):

        if not isinstance(other, Vector2):
            return NotImplemented

        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):

        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)

        elif isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)

        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):

        if not isinstance(other, (int, float)):
            return NotImplemented

        return Vector2(self.x / other, self.y / other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def __eq__(self, other):

        if not isinstance(other, Vector2):
            return False

        return self.x == other.x and self.y == other.y

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, index):

        if index == 0:
            return self.x

        elif index == 1:
            return self.y

        else:
            raise IndexError("Vector2 index out of range")


class Direction(Enum):
    NORTH = (0, 1)
    SOUTH = (0, -1)
    EAST = (1, 0)
    WEST = (-1, 0)