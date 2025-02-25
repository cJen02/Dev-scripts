import torch
import torch.nn as nn
import torch.optim as optim

# Sample training data: y = 2x + 1
X_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]], dtype=torch.float32)
y_train = torch.tensor([[3.0], [5.0], [7.0], [9.0]], dtype=torch.float32)

# Define a simple neural network
class SimpleMLP(nn.Module):
    def __init__(self):
        super(SimpleMLP, self).__init__()
        self.fc = nn.Linear(1, 1)  # Single-layer linear model

    def forward(self, x):
        return self.fc(x)

# Initialize model, loss function, and optimizer
model = SimpleMLP()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
epochs = 100
for epoch in range(epochs):
    optimizer.zero_grad()
    predictions = model(X_train)
    loss = criterion(predictions, y_train)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# Test the model
X_test = torch.tensor([[5.0]], dtype=torch.float32)
y_pred = model(X_test).item()
print(f"Prediction for input 5: {y_pred:.4f}")
