from .vector2d import *

class Line2D:
    def __init__(self , p1:'Vector2D' , p2:'Vector2D') -> None:
        self.p1=p1
        self.p2=p2
    def __str__(self):
        return f"({self.p1}, {self.p2})"

    def __repr__(self):
        return f"({self.p1}, {self.p2})"

    def __eq__(self , l2):
        try:
            if self.p1 == l2.p1 and self.p2 == l2.p2:
                return True
            else:
                return False
        except:
            return False

def collision(l1, l2):
    x1 = l1.p1.x
    x2 = l1.p2.x
    y1 = l1.p1.y
    y2 = l1.p2.y
    x3 = l2.p1.x
    x4 = l2.p2.x
    y3 = l2.p1.y
    y4 = l2.p2.y
    den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if den == 0:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
    if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2) and min(x3, x4) <= px <= max(x3, x4) and min(y3, y4) <= py <= max(y3, y4):
        return round(px,10), round(py,10)
    return None


