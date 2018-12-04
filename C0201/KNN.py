import numpy as np
import operator


def euclidean_distance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    return np.sqrt(distance)


def knn(training_set, test_instance, k):
    distances = {}
    length = test_instance.shape[1]

    for x in range(len(training_set)):
        dist = euclidean_distance(test_instance, training_set.iloc[x], length)
        distances[x] = dist[0]

    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))

    neighbors = []

    for x in range(k):
        neighbors.append(sorted_d[x][0])
    class_votes = {}

    for x in range(len(neighbors)):
        response = training_set.iloc[neighbors[x]][-1]

        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1

    sortedVotes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0], neighbors
