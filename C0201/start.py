import pandas as pd
from DMC import dmc
from KNN import knn
from NN import nn

data = pd.read_csv("iris.csv")
testSet = [[7.2, 3.6, 5.1, 2.5]]
test = pd.DataFrame(testSet)

k = 5
result1, neighbor1 = nn(data, test)
result2, neighbor2 = knn(data, test, k)
result3, neighbor3 = dmc(data, test)

print("\nResultados: ")
print("NN\n\tResults: {} - Vizinho: {}".format(result1, neighbor1))
print("KNN\n\tResults: {} - Vizinho: {}".format(result2, neighbor2))
print("DMC\n\tResults: {} - Vizinho(Centroide): {}".format(result3, neighbor3))