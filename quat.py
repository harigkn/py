import math

class Quaternion(object):
    """Class defining quaternion behaviour."""
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        # Some definitions for the vector and the angle
        self.t = math.acos(w)*2
        self.v = x,y,z
    def __mul__(self, other):
        w1, x1, y1, z1 =  self.w,  self.x,  self.y,  self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        return self.__class__( w1*w2 - x1*x2 - y1*y2 - z1*z2,
                               w1*x2 + x1*w2 + y1*z2 - z1*y2,
                               w1*y2 - x1*z2 + y1*w2 + z1*x2,
                               w1*z2 + x1*y2 - y1*x2 + z1*w2 )
    def __add__(self, other):
        return self.__class__( self.w + other.w,
                               self.x + other.x,
                               self.y + other.y,
                               self.z + other.z )

