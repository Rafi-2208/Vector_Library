import math


class Vector2D:
    def __init__(self, arr: tuple[float, float] | list[float]):
        self.x = arr[0]
        self.y = arr[1]
        if len(arr) != 2:
            raise TypeError("Vector2D can only be of length 2")

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x + other.x, self.y + other.y])
        return Vector2D([round(self.x + other, 10), round(self.y + other, 10)])

    def __radd__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x + other.x, self.y + other.y])
        return Vector2D([round(self.x + other, 10), round(self.y + other, 10)])

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x - other.x, self.y - other.y])
        return Vector2D([round(self.x - other, 10), round(self.y - other, 10)])

    def __rsub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x - other.x, self.y - other.y])
        return Vector2D([round(self.x - other, 10), round(self.y - other, 10)])

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x * other.x, self.y * other.y])
        return Vector2D([round(self.x * other, 10), round(self.y * other, 10)])

    def __rmul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x * other.x, self.y * other.y])
        return Vector2D([round(self.x * other, 10), round(self.y * other, 10)])

    def __truediv__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x / other.x, self.y / other.y])
        return Vector2D([round(self.x / other, 10), round(self.y / other, 10)])

    def __rtruediv__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x / other.x, self.y / other.y])
        return Vector2D([round(self.x / other, 10), round(self.y / other, 10)])

    def __floordiv__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x // other.x, self.y // other.y])
        return Vector2D([round(self.x // other, 10), round(self.y // other, 10)])

    def __rfloordiv__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x // other.x, self.y // other.y])
        return Vector2D([round(self.x // other, 10), round(self.y // other, 10)])

    def __mod__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x % other.x, self.y % other.y])
        return Vector2D([round(self.x % other, 10), round(self.y % other, 10)])

    def __rmod__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x % other.x, self.y % other.y])
        return Vector2D([round(self.x % other, 10), round(self.y % other, 10)])

    def __pow__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x ** other.x, self.y ** other.y])
        return Vector2D([round(self.x ** other, 10), round(self.y ** other, 10)])

    def __rpow__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x ** other.x, self.y ** other.y])
        return Vector2D([round(self.x ** other, 10), round(self.y ** other, 10)])

    def length(self) -> float:
        """Returns length of vector"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def norm(self) -> 'Vector2D':
        """Returns normalised vector"""
        return self / self.length()

    def __lt__(self, other):
        if isinstance(other, Vector2D):
            return self.length() < other.length()
        return self.length() < other

    def __le__(self, other):
        if isinstance(other, Vector2D):
            return self.length() <= other.length()
        return self.length() <= other

    def __gt__(self, other):
        if isinstance(other, Vector2D):
            return self.length() > other.length()
        return self.length() > other

    def __ge__(self, other):
        if isinstance(other, Vector2D):
            return self.length() >= other.length()
        return self.length() >= other

    def __neg__(self):
        return Vector2D([-self.x, -self.y])

    def __abs__(self):
        return Vector2D([abs(self.x), abs(self.y)])

    def __bool__(self):
        if self.x != 0 or self.y != 0:
            return True
        return False

    def rotate(self, a: float , point:'Vector2D' = None) -> 'Vector2D':
        """Returns vector rotated by angle in degrees.\n\nOptional argument "point" allows for rotation around specific point."""
        a = a * math.pi / 180
        if point is None:
            return Vector2D((round(self.x * math.cos(a) - self.y * math.sin(a), 10),
                         round(self.x * math.sin(a) + self.y * math.cos(a), 10)))
        else:
            v = self - point
            return Vector2D((round(v.x * math.cos(a) - v.y * math.sin(a) + point.x, 10),
                         round(v.x * math.sin(a) + v.y * math.cos(a) + point.y, 10)))

def dot(v1: Vector2D, v2: Vector2D) -> float:
    """Returns dot product of two vectors"""
    return round(v1.x * v2.x + v1.y * v2.y, 10)


def cross(v1: Vector2D, v2: Vector2D) -> float:
    """Returns cross product of two vectors"""
    return round(v1.x * v2.y - v1.y * v2.x, 10)


def angle(v1: Vector2D, v2: Vector2D = None, mode: str = 'd') -> float:
    """Returns the angle between two vectors (-180 to 180 range counter-clockwise being positive).\n\n If only one vector is given returns angle from positive x-axis.\n\nHas 2 modes 'd' and 'r' which return angle in degrees or radians respectively (default mode is degrees)."""
    if v2 is None:
        v2 = Vector2D([1, 0])
    if mode == 'd':
        conversion = 180 / math.pi
    elif mode == 'r':
        conversion = 1
    else:
        raise ValueError("mode can only be 'd'(degrees) or 'r'(radians)")
    c = cross(v1, v2)
    if c > 0:
        conversion = -conversion
    return round(math.acos(dot(v1, v2) / v1.length() * v2.length()) * conversion, 10)


def project(v1: Vector2D, v2: Vector2D) -> tuple[Vector2D, Vector2D]:
    """Returns vector projected from vector v1 to vector v2 and remaining vector perpendicular to vector v2"""
    parallel = dot(v1, v2) / (v2.length() ** 2) * v2
    return parallel, v1 - parallel


def reflect(v1: Vector2D, v2: Vector2D) -> Vector2D:
    """Returns vector v1 reflected in vector v2"""
    parallel, perpendicular = project(v1, v2)
    return parallel - perpendicular



# -----testing area-----
if __name__ == "__main__":
    pass
