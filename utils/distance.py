from ..core.vector import Vector
from ..core.cluster import Cluster
import math


def euclidian_distance(a, b):
    if isinstance(a, Vector) and isinstance(b, Vector):
        delta = (a- b)**2
        return math.sqrt(delta.sum())
    elif isinstance(a, Cluster) and isinstance(b, Cluster):
        delta = (a.centroid - b.centroid)**2
        return math.sqrt(delta.sum())
    else:
        raise TypeError(
            f"Arguments must be either Vector or Cluster. a: {type(a)} b: {type(b)}")
