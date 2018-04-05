import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

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
     
    # Determine the variance & bias
    predictions = model.predict(filtered_cars[cols])
    variance = np.var(predictions)
    mse = mean_squared_error(y_true=filtered_cars['mpg'], y_pred=predictions)
     
    return mse, variance
 

one_mse, one_var = train_and_test(["cylinders"])
two_mse, two_var = train_and_test(["cylinders", "displacement"])
three_mse, three_var = train_and_test(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_test(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin"])

error_dict = {'variables': [1,2,3,4,5,6,7], 
              'mse': [one_mse,two_mse,three_mse,four_mse,five_mse,six_mse,seven_mse],
              'variance': [one_var,two_var,three_var,four_var,five_var,six_var,seven_var]}

print('in-sample error')
error_df = pd.DataFrame(error_dict)
print(error_df)

#          mse  variables   variance
# 0  24.020180          1  36.742559
# 1  21.282057          2  39.480681
# 2  20.252955          3  40.509784
# 3  17.763861          4  42.998878
# 4  17.761396          5  43.001342
# 5  11.590171          6  49.172567
# 6  10.847481          7  49.915257

fig = plt.figure()
plt.scatter(error_df['variables'],error_df['mse'],label='mse',color='red')
plt.scatter(error_df['variables'],error_df['variance'],label='variance',color='blue')
plt.legend()
plt.title('in-sample error')
plt.show()