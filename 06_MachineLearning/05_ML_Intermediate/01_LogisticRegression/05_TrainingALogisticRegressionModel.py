# Recall that the gpa column contains the GPA of each applicant as a real value between 0.0 and 4.0
# the admit column specifies if that applicant was admitted (0 if not admitted and 1 if admitted).
import pandas as pd
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv('admissions.csv')

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])