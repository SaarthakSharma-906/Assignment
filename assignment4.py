import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Display the first few rows of the dataset
print(titanic.head())

# Step 1: Data Preprocessing

# 1.1 Handling Missing Values
print(titanic.isnull().sum())

# Fill missing 'age' values with the median age
titanic['age'].fillna(titanic['age'].median(), inplace=True)

# Fill missing 'embarked' values with the most common port
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

# Drop 'deck' and 'embark_town' columns due to a high number of missing values
titanic.drop(['deck', 'embark_town'], axis=1, inplace=True)

# Drop rows where 'embarked' is missing
titanic.dropna(subset=['embarked'], inplace=True)

# 1.2 Converting Categorical Variables to Numeric
# Convert 'sex' to numeric
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})

# Convert 'embarked' to numeric using one-hot encoding
titanic = pd.get_dummies(titanic, columns=['embarked'], drop_first=True)

# 1.3 Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
titanic[['age', 'fare']] = scaler.fit_transform(titanic[['age', 'fare']])

# Step 2: Feature Engineering

# 2.1 Creating new features
# Create 'family_size' feature
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1

# Create 'is_alone' feature
titanic['is_alone'] = np.where(titanic['family_size'] > 1, 0, 1)

# 2.2 Simplifying existing features
# Simplify 'pclass' to 'pclass_1', 'pclass_2', 'pclass_3'
titanic = pd.get_dummies(titanic, columns=['pclass'], drop_first=True)

# Drop unused columns
titanic.drop(['who', 'adult_male', 'alive', 'class', 'embarked', 'sibsp', 'parch', 'deck', 'embark_town', 'alone'], axis=1, inplace=True)

# Display the first few rows of the preprocessed dataset
print(titanic.head())

# Save the preprocessed dataset to a new CSV file
titanic.to_csv('titanic_preprocessed.csv', index=False)
