import numpy as np

def euclidean_distance(p1, p2):
    return np.linalg.norm(p1 - p2)

def calculate_centroids(data, centroids):
    clusters = [[] for _ in centroids]

    # Assign data points to the nearest centroid
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        min_distance = min(distances)
        min_indices = [i for i, distance in enumerate(distances) if distance == min_distance]

        if len(min_indices) > 1:
            clusters[0].append(point)  # Assign to cluster with centroid (0, 0)
        else:
            cluster_idx = min_indices[0]
            clusters[cluster_idx].append(point)

    # Calculate new centroids
    new_centroids = []
    for cluster in clusters:
        if len(cluster) > 0:
            new_centroid = np.mean(cluster, axis=0)
            new_centroids.append(new_centroid)
        else:
            #If none of the data points were assigned to the given centroid, return None
            new_centroids.append([None,None])
        
    return np.array(new_centroids)

def has_none(arr): 
    return np.any(np.equal(arr, None))


def main():
    # Read input
    n = int(input())
    data = []
    for _ in range(n):
        x, y = map(float, input().split())
        data.append([x, y])
    data = np.array(data)

    # Initial centroids
    centroids = np.array([[0, 0], [2, 2]])

    # Calculate centroids
    new_centroids = calculate_centroids(data, centroids)

    for centroid in new_centroids:
        if not has_none(centroid):
            """
            # print(centroid.round(2)) won't work
            # print(np.round(centroid,2)) won't work
            #Because You cannot round numpy arrays that are objects, this can be changed with astype as long as your array can be safely converted to floats:

            a = np.random.rand(5).astype(np.object)
            #array([0.5137250555772075, 0.4279757819721647, 0.4177118178603122,0.6270676923544128, 0.43733218329094947], dtype=object)
            np.around(a,3)

            #ValueError: invalid literal for int() with base 10: "AttributeError: 'float' object has no attribute 'rint'"        
            """
            print(np.around(centroid.astype(np.double),2))
        else:
            print(None)

if __name__=='__main__':
    main()
