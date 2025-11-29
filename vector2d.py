
class Vector2D:
    def __init__(self, arr):
        self.x = arr[0]
        self.y = arr[1]
        if len(arr) != 2:
            raise TypeError("Vector2D can only be of length 2")
    def __add__(self, other):
        return Vector2D([self.x + other.x, self.y + other.y])
    def __radd__(self, other:float):
        return Vector2D([self.x + other, self.y + other])
    def __sub__(self, other):
        return Vector2D([self.x - other.x, self.y - other.y])
    def __rsub__(self, other: float):
        return Vector2D([self.x - other, self.y - other])
    def __mul__(self, other):
        return Vector2D([self.x * other.x, self.y * other.y])
    def __rmul__(self, other: float):
        return Vector2D([self.x * other, self.y * other])
    def __truediv__(self, other):
        return Vector2D([self.x / other.x, self.y / other.y])
    def __rtruediv__(self, other: float):
        return Vector2D([self.x / other, self.y / other])
    def __floordiv__(self, other):
        return Vector2D([self.x // other.x, self.y // other.y])
    def __rfloordiv__(self, other:float):
        return Vector2D([self.x // other, self.y // other])
    def __mod__(self, other):
        return Vector2D([self.x % other.x, self.y % other.y])
    def __rmod__(self, other: float):
        return Vector2D([self.x % other, self.y % other])
    def __rpow__(self, other : float):
        return Vector2D([self.x ** other, self.y ** other])

#-----testing area-----
if __name__ == "__main__":
    import time
    import numpy as np
    a = Vector2D([1, 2, 3])
    a = [4,8]
    t = time.time()
    v = Vector2D(a)
    for i in range(10000):
        z = v + v
    print(time.time() - t)
    v = np.array(a)
    for i in range(10000):
        z = v + v
    print(time.time() - t)