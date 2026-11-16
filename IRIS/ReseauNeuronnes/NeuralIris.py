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
    training_data = data[:40] + data[50:90] + data[100:140]
    rd.shuffle(training_data) # Shuffling of training data
    training_set = np.array([[float(x0),float(x1),float(x2),float(x3)] for x0,x1,x2,x3,_ in training_data])
    training_labels = np.array([[float(x4=="Iris-setosa"),float(x4=="Iris-versicolor"),float(x4=="Iris-virginica")] for _,_,_,_,x4 in training_data])
    testing_data = data[40:50] + data[90:100] + data[140:150]
    testing_set = np.array([[float(x0),float(x1),float(x2),float(x3)] for x0,x1,x2,x3,_ in testing_data])
    testing_labels = np.array([[float(x4=="Iris-setosa"),float(x4=="Iris-versicolor"),float(x4=="Iris-virginica")] for _,_,_,_,x4 in testing_data])
    mean = training_set.mean(axis=0)
    std = training_set.std(axis=0)
    training_set = (training_set - mean) / std
    testing_set = (testing_set - mean) / std # Normalisation only on training data, avoids leaking testing data information
    #print(training_set, training_set.mean(axis=0), training_set.std(axis=0))

# Param Init, input(4,1), 1 hidden layer(8,4) with sigmoide, output(3,8) with softmax

np.random.seed(42)
W1 = np.random.randn(8, 4) * 0.1  # hidden_layer (8, 4)
b1 = np.zeros(8)  # biais (8,)
W2 = np.random.randn(3, 8) * 0.1  # output (3, 8)
b2 = np.zeros(3)  # hidden_biais (3,)


def sigmoide(M):
    return 1/(1+np.exp(-M))

def softMax(M):
    exp_M = np.exp(M - np.max(M))
    return exp_M / exp_M.sum()

def forward_pass(input):
    A1 = sigmoide(W1 @ input + b1)
    A2 = softMax(W2 @ A1 + b2)
    return A1, A2

def is_misclasified(training_set,labels,cost=0.1):
    for i in range(training_set.__len__):
        if ((forward_pass(training_set[i]) - labels[i])**2).sum() > cost:
            return False
    return True #Cost must be inferior to 0.1

def train_neural_network(epochs, lr, W1, b1, W2, b2):
    for epoch in range(epochs):
        for i in range(len(training_set)):
            x, y = training_set[i],training_labels[i]

            # ForwardPass
            A1, A2 = forward_pass(x)

            #BACK_PROPAGATION
            dZ2 = A2 - y
            dW2 = np.outer(dZ2, A1)  # (3, 1) x (1, 8) -> (3, 8)
            db2 = dZ2  # (3,1)

            # Backpropagation hidden layer
            dZ1 = (W2.T @ dZ2) * (A1 * (1 - A1))  # (8,1)
            dW1 = np.outer(dZ1, x)  # (8, 1) x (1, 4) -> (8, 4)
            db1 = dZ1  # (8,1)

            # Update
            W2 -= lr * dW2
            b2 -= lr * db2
            W1 -= lr * dW1
            b1 -= lr * db1

train_neural_network(5,0.05,W1,b1,W2,b2)

# TESTING
correct = 0
for i in range(len(testing_set)):
  _, pred = forward_pass(testing_set[i])
  print(pred, testing_labels[i])
  if np.argmax(pred) == np.argmax(testing_labels[i]):
    correct += 1

print(correct/len(testing_set))