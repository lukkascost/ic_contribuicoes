import numpy as np
import operator
import pandas as pd


def euclidean_distance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    return np.sqrt(distance)


def dmc(training_set, test_instance):
    classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    centroids = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
    cont = 0
    for x in range(len(classes)):
        for y in range(len(training_set)):
            current = [training_set.iloc[y]['SepalLength'], training_set.iloc[y]['SepalWidth'],
                       training_set.iloc[y]['PetalLength'], training_set.iloc[y]['PetalWidth']]
            iris_class = training_set.iloc[y][-1]
            if iris_class == classes[x]:
                cont += 1
                centroids[x] = [centroids[x][0] + current[0], centroids[x][1] + current[1],
                                centroids[x][2] + current[2], centroids[x][3] + current[3]]

        for i in range(len(centroids[x])):
            centroids[x][i] = centroids[x][i] / cont

        centroids[x].append(classes[x])
        cont = 0

    test_centroid = pd.DataFrame(centroids)
    distances = {}

    length = test_instance.shape[1]
    for x in range(len(test_centroid)):
        dist = euclidean_distance(test_instance, test_centroid.iloc[x], length)
        distances[x] = dist[0]

    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))

    neighbor = sorted_d[0][0]
    response = test_centroid.iloc[neighbor][4]

    return response, neighbor
