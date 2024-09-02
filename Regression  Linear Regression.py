import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([59, 70, 99, 116, 138, 150, 176]).reshape(-1, 1) # House size ine ing m)
y = np.array([159000 , 280969, 25966600, 399999,3599990,400000 , 4588889])
# Create and fit the mode
model = LinearRegression()
model.fit(X, y)
X_new = np.array([80, 120, 160]).reshape(-1, 1)
y_pred = model.predict(X_new)

plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.scatter(X_new,y_pred, color='green', label= ' Predictions')
plt.xlabel('House Size(sq m) ' )
plt.ylabel('House Price ($)')
plt.legend()
plt.show()
print(f"Predicted prices for houses of size 89, 128, and 160 sq m: {y_pred}")