import pandas as pd
# read the CSV file into a pandas DataFrame
df = pd.read_csv('group-selfies-10m-output.csv')

# get the number of rows in the DataFrame using the shape attribute
line_count = df.shape[0]

print(df.describe())