from .vector import Vector
import statistics


class Cluster:
    def __init__(self, data: list = [], centroid=None) -> None:
        if not isinstance(data, list):
            raise TypeError(
                f"Wrong type: {type(data)}. Argument must be a list")
        self.data = data
        self.centroid = centroid or self.__calculate_centroid()
    
    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        if isinstance(key, (int, slice)):
            return self.data[key]
        else:
            raise KeyError(f"Invalid key: {key}")

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f"Cluster({[str(vec) for vec in self.data]})"
    
    def __calculate_centroid(self):
        return Vector([sum(v) for v in zip(*self.data)]) / len(self.data)


    def append(self, data):
        if isinstance(data, Vector):
            self.data.append(data)
            self.centroid = self.__calculate_centroid()
        else:
            raise TypeError(f"Wrong type: {type(data)}")
    
    def extend(self, data):
        if isinstance(data, Cluster):
            for v in data:
                self.data.append(v)
            self.centroid = self.__calculate_centroid()
        else:
            raise TypeError(f"Wrong type: {type(data)}")

    def wcss(self):
        total = 0
        for v in self.data:
            total += sum(v.data)
        return total



    def sum(self):
        total = 0
        for v in self.data:
            total += sum(v.data)
        return total
