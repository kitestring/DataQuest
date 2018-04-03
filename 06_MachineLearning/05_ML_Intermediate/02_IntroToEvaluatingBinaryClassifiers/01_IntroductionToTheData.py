import pandas as pd
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")
model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])
labels = model.predict(admissions[["gpa"]])

admissions['predicted_label'] = labels
value_counts = admissions['predicted_label'].value_counts()

print(value_counts.head(5))