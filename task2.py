import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# --- Basic Info ---
print("Initial Shape:", df.shape)
print("Missing Values:\n", df.isnull().sum())

# --- Data Cleaning ---
df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Convert data types
df['Pclass'] = df['Pclass'].astype('category')
df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')

# --- Univariate Plots ---
sns.countplot(x='Survived', data=df)
plt.title('Survival Count'); plt.show()

sns.histplot(x='Age', data=df, bins=30, kde=True)
plt.title('Age Distribution'); plt.show()

sns.histplot(x='Fare', data=df, bins=40, kde=True)
plt.title('Fare Distribution'); plt.show()

# --- Bivariate Analysis ---
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Gender'); plt.show()

sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival by Class'); plt.show()

sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age vs Survival'); plt.show()

sns.countplot(x='Embarked', hue='Survived', data=df)
plt.title('Survival by Embarkation'); plt.show()

# --- Correlation Heatmap ---
numeric_corr = df.corr(numeric_only=True)
sns.heatmap(numeric_corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix'); plt.show()

# --- Crosstabs (printed insights) ---
print("\nSurvival % by Gender:\n", pd.crosstab(df['Sex'], df['Survived'], normalize='index') * 100)
print("\nSurvival % by Class:\n", pd.crosstab(df['Pclass'], df['Survived'], normalize='index') * 100)
print("\nSurvival % by Embarked:\n", pd.crosstab(df['Embarked'], df['Survived'], normalize='index') * 100)
