import numpy as np
import operator


def euclidean_distance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    return np.sqrt(distance)


def nn(training_set, test_instance):
    distances = {}
    length = test_instance.shape[1]

    for x in range(len(training_set)):
        dist = euclidean_distance(test_instance, training_set.iloc[x], length)
        distances[x] = dist[0]

    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))

    neighbor = sorted_d[0][0]
    response = training_set.iloc[neighbor][-1]

    return response, neighbor
