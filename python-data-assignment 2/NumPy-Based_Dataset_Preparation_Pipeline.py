import numpy as np

np.random.seed(0)

data = np.random.randn(100, 3)
print(f"Original Data Shape: ", data.shape)

mean = data.mean(axis=0)
print(f"Mean Shape: ", mean.shape)

std = data.std(axis=0)
print(f"Standard Deviation Shape: ", std.shape)

normalized = (data - mean) / std
split = int (0.8 * len(normalized))
train = normalized[: split]
test = normalized[split :]

train [0, 0] = 999

print("Training Data Shape: ", train.shape)
print("Test Data Shape: ", test.shape)
print("Note: Modifying the slice affected the original array")