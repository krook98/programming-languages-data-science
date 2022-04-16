import pandas as pd

df = pd.read_csv('QueryResults.csv')

# Posts per language on StackOverflow
df.groupby('TagName').sum()

# How many months of data?
df.groupby('TagName').count()