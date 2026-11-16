import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math
import csv

# Preprocessing data, normalisation
with open("IRIS/iris/iris.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    # Data : sepal length ; sepal width ; petal length ; petal width ; label
    data = list(reader)
    data.pop()
    N = 150
    Mean = np.array([5.84,3.05,3.76,1.20])
    S = np.array([0.83,0.43,1.76,0.76])
    training_data = []
    for i in range(N):
        [x0,x1,x2,x3,label] = data[i]

        x0 = (float(x0) - Mean[0])/S[0]
        x1 = (float(x1) - Mean[1])/S[1]
        x2 = (float(x2) - Mean[2])/S[2]
        x3 = (float(x3) - Mean[3])/S[3]

        if label == "Iris-setosa":
            label = 0
        elif label == "Iris-versicolor":
            label = 1
        elif label == "Iris-virginica":
            label = 2

        training_data.append([x0,x1,x2,x3,label])

    training_set = training_data[:40] + training_data[50:90] + training_data[100:140]
    testing_set = training_data[40:50] + training_data[90:100] + training_data[140:150]

    #print(training_set)
    #print(testing_set)
    #print(np.mean(training_data,axis=0))
    #print(np.var(training_data,axis=0)) #The data is normalised !Label is not

# The parametres, 4 inputs, 2 hidden layers , 3 outputs

biais0 = [rd.random() for i in range(5)]
H1 = np.array([[rd.random(),rd.random(),rd.random(),rd.random()] for i in range(5)]) # 5 * 4
hbiais1 = [rd.random() for i in range(5)]
H2 = np.array([[rd.random(),rd.random(),rd.random(),rd.random(),rd.random()] for i in range(5)]) # 5 * 5
hbiais2 = [rd.random() for i in range(3)]
output = np.array([[rd.random(),rd.random(),rd.random(),rd.random(),rd.random()] for i in range(3)]) # 3 * 5

def sigmoide(f):
    return 1/(1+math.exp(f))

def is_misclasified(input):
return (hbiais2 + output @ (hbiais1 + H2 @ (biais0 + H1 @ input[:5])))