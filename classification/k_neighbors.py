from ..core.frame import Frame
from ..core.vector import Vector
from ..utils.distance import euclidian_distance
from collections import Counter

class KNeighbors:
    def __init__(self, k) -> None:
        self.k = k
    
    def fit(self, data:Frame):
        self.data = data

    def classify(self, to_classify: Frame | Vector):
        if isinstance(to_classify, Frame):
            pass

        if isinstance(to_classify, Vector):
            distances = []
            for i, vector in enumerate(self.data):
                distances.append((i, euclidian_distance(to_classify, vector)))
            
            distances.sort(key=lambda x: x[1])
            closest_indexes = distances[:self.k]
            category_freq = [self.data.labels[i] for i, _ in closest_indexes]
            print(category_freq)
            return Counter(category_freq).most_common(1)[0][0]

                


        




    

        