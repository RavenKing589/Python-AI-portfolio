# data_analysis.py
import pandas as pd


# Load data
df = pd.read_csv("Titanic.csv")
print(df.head())
print(df.info())

import matplotlib.pyplot as plt
import seaborn as sns

 # set Style
sns.set_theme(style="whitegrid")
# chart 1: Survival Rate by Sex
plt.figure(figsize=(8,5))
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by sex')
plt.xlabel('sex (0=Male, 1=Female)')
plt.ylabel('Survival Rate')
plt.ylim(0,1)
plt.show()

# chart 2: Survival by Class
plt.figure(figsize=(8,5))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('surivival Rate by PassengerClass')
plt.xlabel('Class')
plt.ylabel('Survival Rate')
plt.ylim(0,1)
plt.show()

# Chart 3: Age Distribution by Survival
plt.figure(figsize=(10,5))
sns.histplot(data=df, x='Age', hue='Survived', bins=30, alpha=0.7)
plt.title('Age Distribution: Survived vs Not')
plt.xlabel('Age')
plt.legend(['Died', 'Survived'])
plt.show()

