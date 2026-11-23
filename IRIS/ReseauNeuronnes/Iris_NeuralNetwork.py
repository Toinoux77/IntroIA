import matplotlib.pyplot as plt
import numpy as np
import random as rd
import csv

# Preprocessing data, normalisation
with open("IRIS/iris/iris.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    # Data : sepal length ; sepal width ; petal length ; petal width ; label
    data = list(reader)
    data.pop()
    N=150
    training_data = data[:30] + data[50:80] + data[100:130]
    rd.shuffle(training_data) # Shuffling of training data
    training_set = np.array([[float(x0),float(x1),float(x2),float(x3)] for x0,x1,x2,x3,_ in training_data])
    training_labels = np.array([[float(x4=="Iris-setosa"),float(x4=="Iris-versicolor"),float(x4=="Iris-virginica")] for _,_,_,_,x4 in training_data])
    testing_data = data[30:50] + data[80:100] + data[130:150]
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

def compute_loss(X, Y):
  total_loss = 0.0
  for i in range(len(X)):
    _, pred = forward_pass(X[i])
    total_loss += -np.sum(Y[i] * np.log(pred + 1e-15))
  return total_loss / len(X)

def train_neural_network(epochs=500, lr=0.05):
  global W1, b1, W2, b2
  train_loss_history = []
  test_loss_history = []

  print(f"{'Époque':<10} | {'Train Loss':<12} | {'Test Loss':<12}")
  print("-" * 38)

  for epoch in range(1, epochs + 1):
    epoch_train_loss = 0.0

    for i in range(len(training_set)):
      x = training_set[i]
      y = training_labels[i]

      A1, A2 = forward_pass(x)
      epoch_train_loss += -np.sum(y * np.log(A2 + 1e-15))

      dZ2 = A2 - y
      dW2 = np.outer(dZ2, A1)
      db2 = dZ2

      dZ1 = (W2.T @ dZ2) * (A1 * (1 - A1))
      dW1 = np.outer(dZ1, x)
      db1 = dZ1

      W2 -= lr * dW2
      b2 -= lr * db2
      W1 -= lr * dW1
      b1 -= lr * db1

    mean_train_loss = epoch_train_loss / len(training_set)
    mean_test_loss = compute_loss(testing_set, testing_labels)

    train_loss_history.append(mean_train_loss)
    test_loss_history.append(mean_test_loss)

    if epoch == 1 or epoch % 50 == 0:
      print(f"{epoch:<10} | {mean_train_loss:<12.4f} | {mean_test_loss:<12.4f}")

  return train_loss_history, test_loss_history

train_losses, test_losses = train_neural_network()

# TESTING
correct = 0
for i in range(len(testing_set)):
    _, pred = forward_pass(testing_set[i])
    if np.argmax(pred) == np.argmax(testing_labels[i]):
        correct += 1
        print(pred, testing_labels[i])
    else:
        print(f"\033[31m{pred}, {testing_labels[i]}\033[0m")

print(f"Coût final (train) : {train_losses[-1]:.4f}")
print(f"Coût final (test)  : {test_losses[-1]:.4f}")
print(f"Précision sur le jeu de test : {correct}/{len(testing_set)} ({correct/len(testing_set)*100:.1f}%)")

# 5. Tracé comparatif des courbes d'apprentissage
epochs_range = range(1, len(train_losses) + 1)

plt.figure(figsize=(10, 5))
plt.plot(epochs_range, train_losses, color="#1f77b4", linewidth=2, label="Coût d'entraînement (Train)")
plt.plot(epochs_range, test_losses, color="#ff7f0e", linewidth=2, linestyle="--", label="Coût de test (Validation)")

plt.title("Évolution du coût d'entraînement vs coût de test (Base Iris)")
plt.xlabel("Époques")
plt.ylabel("Erreur moyenne (Cross-Entropy Loss)")
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()