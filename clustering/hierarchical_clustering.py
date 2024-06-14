from ..core.vector import Vector
from ..core.cluster import Cluster
from ..utils.distance import euclidian_distance
import numpy as np


class HierarchicalClustering:
    def __init__(self, vectors: list[Vector], n_clusters: int = 1) -> None:
        self.n_clusters = n_clusters
        self.clusters = [(n, Cluster([v])) for n, v in enumerate(vectors)]

    def __get_distances(self, clusters, distances):
        for ki, cluster_i in clusters:
            if ki not in distances:
                distances[ki] = {}
            for kj, cluster_j in clusters:
                if kj not in distances[ki] and kj > ki:
                    distances[ki][kj] = euclidian_distance(cluster_i, cluster_j)
        return distances

    def __get_closest_pair(self, distances):
        min_distance = float("inf")
        closest_pair = None
        for k1, v1 in distances.items():
            for k2, distance in v1.items():
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (k1, k2)
        return [closest_pair[0], closest_pair[1], min_distance]

    def __merge_clusters(self, key1, key2):
        for i, cluster in enumerate(self.clusters):
            if cluster[0] == key1:
                c1 =  self.clusters.pop(i)
                break
        for i, cluster in enumerate(self.clusters):
            if cluster[0] == key2:
                c2 =  self.clusters.pop(i)
                break
        c1[1].extend(c2[1])
        return c1[1]

    def __remove_distances(self, distances, index1, index2):
        if index1 in distances:
            del distances[index1]
        if index2 in distances:
            del distances[index2]
        for k1, v1 in distances.items():
            if index1 in v1:
                del distances[k1][index1]
            if index2 in v1:
                del distances[k1][index2]

        return distances

    def centroid_linkage(self):
        linkage_matrix = []
        distances = {}
        cluster_index = len(self.clusters)
        while len(self.clusters) > self.n_clusters:
            distances = self.__get_distances(self.clusters, distances)
            closest_pair = self.__get_closest_pair(distances)
            merged_cluster = self.__merge_clusters(*closest_pair[:2])
            closest_pair.append(len(merged_cluster))
            self.clusters.append((cluster_index, merged_cluster))
            cluster_index += 1
            distances = self.__remove_distances(distances, *closest_pair[:2])
            linkage_matrix.append(closest_pair)
        
        return linkage_matrix
