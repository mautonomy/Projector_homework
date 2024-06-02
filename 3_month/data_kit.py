# Task 1

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#1.a

zeros_array = np.zeros((4, 3))
print("Array of all zeros:")
print(zeros_array)

ones_array = np.ones((4, 3))
print("\nArray of all ones:")
print(ones_array)

numbers_array = np.arange(12).reshape((4, 3))
print("\nArray with numbers from 0 to 11:")
print(numbers_array)

#b

x = np.arange(1, 101, 1)
F_x = 2 * x**2 + 5

print("\nTabulated values of F(x) = 2x^2 + 5 for x in [1, 100]:")
print(F_x)

# c
x = np.arange(-10, 11, 1)
F_x = np.exp(-x)

print("\nTabulated values of F(x) = e^(-x) for x in [-10, 10]:")
print(F_x)

# Task 2

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
df = pd.read_csv(url)
print("Dataset imported successfully.")

df_selected = df[['Team', 'Yellow Cards', 'Red Cards']]
print("\nSelected columns:")
print(df_selected.head())

num_teams = df['Team'].nunique()
print(f"\nNumber of teams participated in Euro 2012: {num_teams}")

teams_scored_more_than_6 = df[df['Goals'] > 6]
print("\nTeams that scored more than 6 goals:")
print(teams_scored_more_than_6[['Team', 'Goals']])


# Task 3

tips = sns.load_dataset('tips')
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Scatter Plot of Total Bill vs Tip')
plt.show()

sns.lineplot(data=tips, x='size', y='total_bill')
plt.title('Line Plot of Total Bill vs Size')
plt.show()

sns.histplot(data=tips, x='total_bill', bins=20)
plt.title('Histogram of Total Bill')
plt.show()

sns.barplot(data=tips, x='day', y='total_bill')
plt.title('Bar Plot of Total Bill by Day')
plt.show()

sns.boxplot(data=tips, x='day', y='total_bill')
plt.title('Box Plot of Total Bill by Day')
plt.show()

sns.violinplot(data=tips, x='day', y='total_bill')
plt.title('Violin Plot of Total Bill by Day')
plt.show()

sns.pairplot(tips)
plt.suptitle('Pair Plot of Tips Dataset', y=1.02)
plt.show()

corr = tips.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap of Tips Dataset')
plt.show()

sns.countplot(data=tips, x='day')
plt.title('Count Plot of Days')
plt.show()

sns.stripplot(data=tips, x='day', y='total_bill', jitter=True)
plt.title('Strip Plot of Total Bill by Day')
plt.show()

sns.swarmplot(data=tips, x='day', y='total_bill')
plt.title('Swarm Plot of Total Bill by Day')
plt.show()

sns.kdeplot(data=tips, x='total_bill')
plt.title('KDE Plot of Total Bill')
plt.show()
