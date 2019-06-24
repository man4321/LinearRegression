import os
import pandas as pd
obj=pd.read_csv("liniar.csv")
print(obj)

from sklearn.linear_model import LinearRegression
X= obj.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = obj.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regessor.predict(X)  # make predictions
print(Y_pred)

import matplotlib.pyplot as plt
plt.scatter(X,Y);
plt.plot(X,Y_pred, color='red')
plt.show()
