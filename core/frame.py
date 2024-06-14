from .cluster import Cluster
from .vector import Vector
from typing import List

class Frame(Cluster):
    def __init__(self, data: List[Vector] = ..., labels = [] , centroid=None) -> None:
        if all(isinstance(v, Vector) for v in data):
            if len(labels) == len(data):
                super().__init__(data, centroid)
                # self.id = [i for i in range(len(data))]
                self. labels = labels
            else:
                raise Exception("Data and labels size must match")
        else:
                raise TypeError("Data must be a list of Vectors")

    
    def __str__(self):
        return f"Frame({self.data})"
        
