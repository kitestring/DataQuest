import pandas as pd
import sys 

if __name__ == "__main__":
    print("Welcome to a Python script")
else:
    sys.exit
    
def load_data(csv_file, new_cols=None):

    df = pd.read_csv(csv_file)
    if new_cols != None:
        df.columns = new_cols
        # f.columns = ['submission_time', 'upvotes', 'url', 'headline']
    return df

