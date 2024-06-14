import random
from ..core.vector import Vector


def rand_vector(start: int, stop: int, dim: int):
    return Vector([float(random.uniform(start, stop)) for _ in range(dim)])

def randint_vector(start: int, stop: int, dim: int):
    return Vector([random.randint(start, stop) for _ in range(dim)])
