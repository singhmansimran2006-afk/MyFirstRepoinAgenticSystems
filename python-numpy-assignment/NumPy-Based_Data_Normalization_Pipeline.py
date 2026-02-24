import numpy as np

data = np.array([10, 20, 30, 40])
print(f"Original Data: {data}")

mean = np.mean(data)
print(f"Mean: {mean}")

std = np.std(data)
print(f"Standard Deviation: {std}")

normalized = (data - mean) / std
print(f"Normalized Data: {normalized}")

reshaped = normalized.reshape(2, 2)
print(f"Reshaped Data Shaped: {reshaped.shape}")