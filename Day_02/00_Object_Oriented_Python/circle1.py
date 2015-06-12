"""Circuitous LLC - 
    An advanced circle analytics company.
"""

import math

class Circle(object):
    """An advanced circle analytic toolkit"""
    
    version = "0.1"
    spam = 0.5
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        "Perform quadrature on this circle."
        return math.pi * self.radius ** 2

