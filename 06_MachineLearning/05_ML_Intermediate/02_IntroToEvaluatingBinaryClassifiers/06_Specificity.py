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

# print(admissions.head(5))

# Binary Classification outcomes
true_positives = len(admissions[(admissions['actual_label'] == 1) & (admissions['predicted_label'] == 1)])
true_negatives  = len(admissions[(admissions['actual_label'] == 0) & (admissions['predicted_label'] == 0)])
false_positives = len(admissions[(admissions['actual_label'] == 0) & (admissions['predicted_label'] == 1)])
false_negatives  = len(admissions[(admissions['actual_label'] == 1) & (admissions['predicted_label'] == 0)])

print('true_positives:', true_positives)
print('true_negatives:', true_negatives)
print('false_positives:', false_positives)
print('false_negatives:', false_negatives)

sensitivity = true_positives / (true_positives + false_negatives)
print('sensitivity:', sensitivity)

specificity = true_negatives / (true_negatives + false_positives)
print('specificity:', specificity)

# true_positives: 31
# true_negatives: 385
# false_positives: 15
# false_negatives: 213
# sensitivity: 0.12704918032786885
# specificity: 0.9625

print('The sensitivity tells us we are correct ~ 13% of the time\npredicting who will be accepted.')
print('The specificity tells us we are correct ~ 96% of the time\npredicting who will not be accepted (rejected).')