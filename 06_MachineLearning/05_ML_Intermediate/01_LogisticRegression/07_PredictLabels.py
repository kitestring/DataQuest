import pandas as pd
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv('admissions.csv')

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
fitted_labels = logistic_model.predict(X=admissions[["gpa"]])

print(fitted_labels)