import numpy as np
import random as rd
import matplotlib.pyplot as plt

true_hyperplane = np.array([-1, 1]) # h1*x1 + h2*x2 + b = 0 <==> x2 = (-h1*x1 - b)/h2
true_biais = 0.5

def is_misclasified(hyperplane, biais, training_set):
    for training_point in training_set:
        if np.sign(hyperplane @ training_point[0] + biais) != training_point[1]:
            return True
    return False

def generate_training_set(size):
    training_set = []
    for i in range(size):
        x = rd.uniform(-1, 1)
        y = rd.uniform(-1, 1)
        if true_hyperplane @ np.array([x, y]) + true_biais > 0:
            label = 1
        else:
            label = -1
        training_set.append([np.array([x, y]), label])
    return training_set

def train_perceptron(training_set):
    hyperplane = np.array([0, 0])
    biais = 0
    while is_misclasified(hyperplane, biais, training_set):
        for training_point in training_set:
            if np.sign(hyperplane @ training_point[0] + biais) != training_point[1]:
                hyperplane = np.add(hyperplane, np.multiply(training_point[1], training_point[0]))
                biais = np.add(biais, training_point[1])

    return hyperplane, biais

training_set = generate_training_set(100)
hyperplane, biais = train_perceptron(training_set)
print("Learned hyperplane:", hyperplane)
print("Learned biais:", biais)

plt.figure(figsize=(8, 8))
plt.plot([-1, 1], [(-hyperplane[0] * -1 - biais) / hyperplane[1], (-hyperplane[0] * 1 - biais) / hyperplane[1]], 'r-', label='Learned Hyperplane')
plt.plot([-1, 1], [(-true_hyperplane[0] * -1 - true_biais) / true_hyperplane[1], (-true_hyperplane[0] * 1 - true_biais) / true_hyperplane[1]], 'g--', label='True Hyperplane')
for training_point in training_set:
    color = 'b' if training_point[1] == 1 else 'orange'
    plt.scatter(training_point[0][0], training_point[0][1], color=color)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('Perceptron Learning')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()