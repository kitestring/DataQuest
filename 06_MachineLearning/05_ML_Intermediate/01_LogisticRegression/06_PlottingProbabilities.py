# The trained model can return the predicted probability for each row in the training data.
# False = 0, True = 1
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv('admissions.csv')

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])



# Probability that the row belongs to label `0`.
    # pred_probs[:,0]
# Probabililty that the row belongs to label `1`.
    # pred_probs[:,1]
pred_probs = logistic_model.predict_proba(X=admissions[["gpa"]])

fig = plt.figure()

plt.scatter(admissions["gpa"],pred_probs[:,1])
plt.show()