import pandas as pd

if __name__ == "__main__":
    contents = pd.read_csv("data/CRDC2013_14content.csv")
    print(contents.head(5))
    print(contents.size)
    print("Program executed successfully!")
