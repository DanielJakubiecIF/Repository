#Create 3D vectors as a Python class.

import math
from fractions import Fraction


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):       
        return f"Vector({self.x!r}, {self.y!r}, {self.z!r})"
    
    def __eq__(self, other):  
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def __ne__(self, other): 
        return not self == other

    def __add__(self, other):   
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):  
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector(self.x * other, self.y * other, self.z * other)
    
    __rmul__ = __mul__

    def cross(self, other):
        return Vector(self.y *other.z - self.z *other.y,
                      self.z *other.x - self.x *other.z,
                      self.x *other.y - self.y *other.x)

    def length(self):
        return math.sqrt(self * self)   

    def __hash__(self):   
        return hash((self.x, self.y, self.z))   

import math
v = Vector(1, 2, 3)
w = Vector(2, -3, 2)
assert v != w
assert v + w == Vector(3, -1, 5)
assert v - w == Vector(-1, 5, 1)
assert v * w == (2)
assert v.cross(w) == Vector(13, 4, -7)
assert v.length() == math.sqrt(14)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")

def find_axis(v1, v2):
    v3 = v1.cross(v2)
    if v3 == Vector(0, 0, 0):
        raise ValueError("v1 and v2 are parallel")
    d = v3.length()
    v3 = v3 * (1.0 / d)
    return v3

print(find_axis(Vector(2, 0, 0), Vector(0, 2, 0)))
find_axis(v, v)
