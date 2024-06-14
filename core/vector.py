from __future__ import annotations
import statistics
from ..exceptions import DifferentSizeVectors
import math


class Vector():
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, key):
        if isinstance(key, (int)):
            return self.data[key]
        if isinstance(key, (slice)):
            return Vector(self.data[key])
        else:
            raise KeyError(f"Invalid key: {key}")

    def __len__(self):
        return len(self.data)

    def __str__(self) -> str:
        return (f"Vector({self.data})")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.data == other.data
        return False
    
    def __add__(self, other):
        if isinstance(other, int):
            return Vector([a + other for a in self.data])
        if isinstance(other, Vector):
            if len(self.data) != len(other.data):
                raise DifferentSizeVectors
            return Vector([a + b for a, b in zip(self.data, other.data)])
        else:
            return TypeError(f"Wrong type: {type(other)}. Must be an int or Vector")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, int):
            return Vector([a - other for a in self.data])
        if isinstance(other, Vector):
            if len(self.data) != len(other.data):
                raise DifferentSizeVectors
            return Vector([a - b for a, b in zip(self.data, other.data)])
        else:
            raise TypeError(f"Wrong type: {type(other)}. Must be an int or Vector")
    
    def __truediv__(self, other) -> Vector:
        if isinstance(other, int):
            return Vector([a / other for a in self.data])
        if isinstance(other, Vector):
            if len(self.data) != len(other.data):
                raise DifferentSizeVectors
            return Vector([a / b for a, b in zip(self.data, other.data)])
        else:
            raise TypeError(f"Wrong type: {type(other)}. Must be an int or Vector")
    
    def __pow__(self, other):
        if isinstance(other, int):
            return Vector([a**other for a in self.data])
        if isinstance(other, Vector):
            if len(self.data) != len(other.data):
                raise DifferentSizeVectors
            return Vector([a ** b for a, b in zip(self.data, other.data)])
        else:
            raise TypeError(f"Wrong type: {type(other)}. Must be an int or Vector")

    def mean(self):
        return statistics.mean(self.data)

    def sum(self):
        return sum(self.data)
