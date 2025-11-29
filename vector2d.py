class Vector2D:
    def __init__(self, arr):
        self.x = arr[0]
        self.y = arr[1]
        if len(arr) != 2:
            raise TypeError("Vector2D can only be of length 2")

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x + other.x, self.y + other.y])
        return Vector2D([self.x + other, self.y + other])

    def __radd__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x + other.x, self.y + other.y])
        return Vector2D([self.x + other, self.y + other])

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x - other.x, self.y - other.y])
        return Vector2D([self.x - other, self.y - other])

    def __rsub__(self, other: float):
        if isinstance(other, Vector2D):
            return Vector2D([self.x - other.x, self.y - other.y])
        return Vector2D([self.x - other, self.y - other])

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x * other.x, self.y * other.y])
        return Vector2D([self.x * other, self.y * other])

    def __rmul__(self, other: float):
        if isinstance(other, Vector2D):
            return Vector2D([self.x * other.x, self.y * other.y])
        return Vector2D([self.x * other, self.y * other])

    def __truediv__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x / other.x, self.y / other.y])
        return Vector2D([self.x / other, self.y / other])

    def __rtruediv__(self, other: float):
        if isinstance(other, Vector2D):
            return Vector2D([self.x / other.x, self.y / other.y])
        return Vector2D([self.x / other, self.y / other])

    def __floordiv__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x // other.x, self.y // other.y])
        return Vector2D([self.x // other, self.y // other])

    def __rfloordiv__(self, other: float):
        if isinstance(other, Vector2D):
            return Vector2D([self.x // other.x, self.y // other.y])
        return Vector2D([self.x // other, self.y // other])

    def __mod__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D([self.x % other.x, self.y % other.y])
        return Vector2D([self.x % other, self.y % other])

    def __rmod__(self, other: float):
        if isinstance(other, Vector2D):
            return Vector2D([self.x % other.x, self.y % other.y])
        return Vector2D([self.x % other, self.y % other])

    def __rpow__(self, other: float):
        if isinstance(other, Vector2D):
            return Vector2D([self.x ** other.x, self.y ** other.y])
        return Vector2D([self.x ** other, self.y ** other])




# -----testing area-----
if __name__ == "__main__":
    pass