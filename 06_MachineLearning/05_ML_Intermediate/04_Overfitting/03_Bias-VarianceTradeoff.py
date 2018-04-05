import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)
filtered_cars = cars[cars['horsepower'] != '?'].copy()
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype('float')

# Create a function named train_and_test that:
    # Takes in a list of column names in filtered_cars as the sole parameter (cols),
    # Trains a linear regression model using:
        # The columns in cols as the features,
        # The mpg column as the target variable.
    # Uses the trained model to make predictions using the same input it was trained on,
    # Computes the variance of the predicted values and the mean squared error between the predicted values and the actual label (mpg column).
    # Returns the mean squared error value followed by the variance (e.g. return(mse, variance)).
# Use the train_and_test function to train a model using only the cylinders column. Assign the resulting mean squared error value and variance to cyl_mse and cyl_var.
# Use the train_and_test function to train a model using only the weight column. Assign the resulting mean squared error value and variance to weight_mse and weight_var.

def train_and_test(cols):
    # Instantiate the Linear Regression class
     lr = LinearRegression()
    
    # train and test the model 
     model = lr.fit(filtered_cars[cols], filtered_cars['mpg'])
     predictions = model.predict(filtered_cars[cols])
     
    # Determine the variance & bias
     variance = np.var(predictions)
     mse = mean_squared_error(y_true=filtered_cars['mpg'], y_pred=predictions)
     
     return mse, variance
 
cyl_mse, cyl_var =  train_and_test(['cylinders'])
print('The measure of bias - cyl_mse:', cyl_mse)
print('The measure of variance (overfitting) - cyl_var:', cyl_var)

weight_mse, weight_var = train_and_test(['weight'])
print('\nThe measure of bias - weight_mse:', weight_mse)
print('The measure of variance (overfitting) - weight_var:', weight_var)

# cyl_mse: 24.0201795682
# cyl_var: 36.7425588742

# weight_mse: 18.6766165974
# weight_var: 42.0861218449