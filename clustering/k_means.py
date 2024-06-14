from ..core.cluster import Cluster
import random
from ..utils.distance import euclidian_distance
from time import sleep

class KMeans:
    def __init__(self, n_clusters, itr = 4):
        self.n_clusters = n_clusters
        self.clusters = []
        self.itr = itr
    
    def __initialize_centroids(self, data):
        for _ in range(self.n_clusters):
            centroid = random.choice(data)
            self.clusters.append(Cluster([], centroid))
    
    def __get_centroids(self):
        return [c.centroid for c in self.clusters]
    
    def __get_distances(self, data):
        distances = {}
        for k1, p in data.items():
            for k2, c in enumerate(self.clusters):
                if not k1 in distances:
                    distances[k1] = {}
                if not k2 in distances[k1]:
                    distances[k1][k2] = euclidian_distance(p, c.centroid)
        return distances

    def __get_WCSS(self):
        wcss = []
        for cluster in self.clusters:
            for vector in cluster:
                wcss.append(((cluster.centroid - vector) ** 2).sum())
        return sum(wcss)
                
    def fit(self, data):
        data = {k:v for k, v in enumerate(data)}
        wcss = {} # Within-Cluster Sum of Squares
        for _ in range(self.itr):
            self.__initialize_centroids(data)
            while True:
                last_centroids = self.__get_centroids()
                
                for cluster in self.clusters:
                    cluster.data = []

                distances = self.__get_distances(data)

                ## Append point to its respective cluster
                for point_idx, cluster_dic in distances.items():
                    # Find the min distance to a cluster
                    cluster_belongs = min(cluster_dic, key=cluster_dic.get)
                    self.clusters[cluster_belongs].append(data.get(point_idx))
                
                current_centroids = self.__get_centroids()
                
                centroids = zip(last_centroids, current_centroids)

                # Exit when centroids remain the same
                if all([l == c for l, c in centroids]):
                    break
            wcss[self.__get_WCSS()] = self.clusters
            self.clusters = []
        min_wcss = min(wcss)
        # return wcss
        return wcss[min_wcss]
        
        
        