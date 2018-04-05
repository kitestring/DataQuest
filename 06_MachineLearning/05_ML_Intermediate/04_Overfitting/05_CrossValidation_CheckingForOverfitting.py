import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
import numpy as np
import matplotlib.pyplot as plt

columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)
filtered_cars = cars[cars['horsepower'] != '?'].copy()
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype('float')


def train_and_test(cols):
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    
    variance_values = []
    mse_values = []
    
    # Instantiate a KFold class
    kf = KFold(n_splits=10, shuffle=True, random_state=3)

    for train_index, test_index in kf.split(features):
        
        # define the training & test sets
        X_train, X_test = features.iloc[train_index], features.iloc[test_index]
        y_train, y_test = target.iloc[train_index], target.iloc[test_index]
        
        # Instantiate the Linear Regression class
        lr = LinearRegression()
        
        # fit the model & make predictions 
        model = lr.fit(X_train, y_train)
        predictions = model.predict(X_test)
        
        # Determine the variance & bias
        variance_values.append(np.var(predictions))
        mse_values.append(mean_squared_error(y_true=y_test, y_pred=predictions))
        
     
    return np.mean(mse_values), np.mean(variance_values)
 

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

print('out-of-sample error')
error_df = pd.DataFrame(error_dict)
print(error_df)

# out-of-sample error
#          mse  variables   variance
# 0  24.271252          1  35.990071
# 1  21.584370          2  38.902525
# 2  20.655622          3  40.091288
# 3  18.169683          4  42.507644
# 4  18.283039          5  42.598736
# 5  12.099685          6  48.928247
# 6  11.418132          7  49.904314


fig = plt.figure()
plt.plot(error_df['variables'],error_df['mse'],label='mse')
plt.plot(error_df['variables'],error_df['variance'],label='variance')
plt.legend()
plt.show()