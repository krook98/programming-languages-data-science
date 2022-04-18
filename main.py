import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)


# Posts per language on StackOverflow
df.groupby('TAG').sum()

# How many months of data?
df.groupby('TAG').count()

# Changing date data from string type
df.DATE = pd.to_datetime(df.DATE)

# Separate column from table; pivot
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)
# print(reshaped_df.shape)
# print(reshaped_df.head())
# print(reshaped_df.tail())
# print(reshaped_df.count())
# print(reshaped_df.isna().values.any())

# Visualisation
# Average observations
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 9))
plt.xticks(fontsize=14)
plt.yticks(fontsize=5)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of StackO Posts per Day', fontsize=14)
plt.ylim(0, 35000)
[
    plt.plot(
        roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name
    ) for column in roll_df.columns]
plt.legend(fontsize=16)
plt.show()