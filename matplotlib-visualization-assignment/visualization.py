import matplotlib.pyplot as plt
import numpy as np

epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
loss = np.array([1, 0.9, 0.82, 0.75, 0.69, 0.61, 0.58, 0.40, 0.35, 0.26])

plt.figure(figsize=(6,6))
plt.plot(loss, epochs, marker="o")
plt.xlabel("Loss")
plt.ylabel("Epochs")
plt.title("Loss vs Epoch")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,6))
plt.scatter(epochs, loss, marker="x")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Epoch vs Loss")
plt.grid(True)
plt.show()

models = ["Model A", "Model B", "Model C"]
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(6,6))
plt.bar(models, accuracy)
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Accuracy of Models")
plt.show()