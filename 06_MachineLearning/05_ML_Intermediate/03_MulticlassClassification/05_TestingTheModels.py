# origin -- Integer and Categorical. 1: North America, 2: Europe, 3: Asia.

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# read csv files
cars = pd.read_csv('auto.csv')

# create dummy variables for the categorical variables
dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)

# drop the dummy originating columns
cars = cars.drop(['cylinders', 'year'], axis=1)

# Split the shuffled_cars Dataframe into 2 Dataframes: train and test.
# Assign the first 70% of the shuffled_cars to train.
# Assign the last 30% of the shuffled_cars to test.
np.random.seed(1)
shuffled_index = np.random.permutation(cars.index)
shuffled_cars = cars.reindex(shuffled_index)
seventy_percent = round(len(shuffled_cars) * 0.7)
train = shuffled_cars.iloc[0:seventy_percent]
test = shuffled_cars.iloc[seventy_percent:]

# For each value in unique_origins, train a logistic regression model with the following parameters:
    # X: Dataframe containing just the cylinder & year binary columns.
    # y: list (or Series) of Boolean values:
        # True if observation's value for origin matches the current iterator variable.
        # False if observation's value for origin doesn't match the current iterator variable.
# Add each model to the models dictionary with the following structure:
    # key: origin value (1, 2, or 3),
    # value: relevant LogistcRegression model instance.
# For each origin value from unique_origins:
    # Use the LogisticRegression predict_proba function to return the 
    # 3 lists of predicted probabilities for the test set and add to the testing_probs Dataframe.

features = [c for c in train.columns if c.startswith("cyl") or c.startswith("year")]

unique_origins = cars['origin'].unique()
unique_origins.sort()
models = {}
predictions = {}

for origin in unique_origins:
    # Generate boolean list based upon current target
    target = train['origin'] == origin
        
    # instantiate LogisticRegression object
    model = LogisticRegression()
    
    # Train LogisticRegression model & Make Predictions
    model.fit(train[features], target)
    
    # Recall that the predict_proba function returns a 2 dimensional nd array
    # the 0th column is the probability that the prediction is false
    # the 1st column is the probability that the prediction is true
    pred_probs = model.predict_proba(test[features])[:,1]
    
    # Add the model to the dictionaries
    models[origin] = model
    predictions[origin] = pred_probs
    
testing_probs = pd.DataFrame(data=predictions)    
print(testing_probs.head(5))

#           1         2         3
# 0  0.956719  0.040597  0.021645
# 1  0.977887  0.016419  0.027686
# 2  0.275721  0.363830  0.357304
# 3  0.982960  0.015573  0.021224
# 4  0.339179  0.267854  0.379375

    
    
    
    
    
    
    
    
    