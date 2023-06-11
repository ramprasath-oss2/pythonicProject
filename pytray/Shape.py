#  Using the Object-Oriented Programming Concepts
#  Creating Shapes to this file 
#  Implementing those shapes where it is necessery

from __init__ import *
from main import *
from logics import *


class Shape: # type: ignore
    pass


class Shape:

    def __init__(self, shape) -> None:
        self.shape = shape

    def __str__(self) -> str:
        return self.shape


class Circle:

    _pi = PI

    def __init__(self, radius) -> None:
        self.radius = radius
        self.diameter = self.radius * 2

    def circumference(self):
        return 2 * self._pi * self.radius 
    
    def area(self):
        return self._pi * (self.radius ** 2)
    
    def Diameter(self):
        return self.diameter
    
    def getChord(self, perdistance: int):
        return 2 * sqrt( (self.radius**2) - (perdistance**2) )


