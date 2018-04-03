import pandas as pd
from sklearn.linear_model import LogisticRegression

# Read csv file
admissions = pd.read_csv("admissions.csv")

# instantiate LogisticRegression object
model = LogisticRegression()

# Train & Test LogisticRegression model
model.fit(admissions[["gpa"]], admissions["admit"])
labels = model.predict(admissions[["gpa"]])
admissions['predicted_label'] = labels

# Check the accuracy of the model
admissions = admissions.rename(columns = {'admit':'actual_label'})
admissions['Matches'] = admissions['predicted_label'] == admissions['actual_label']
correct_predictions = admissions[admissions['Matches'] == True]
print(correct_predictions.head(5))

accuracy = len(correct_predictions) / len(admissions)
print('accuracy:', accuracy)

# accuracy: 0.6459627329192547