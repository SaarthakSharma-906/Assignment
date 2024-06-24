import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target
iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(iris_df.head())

# Summary statistics
print("\nSummary statistics:")
print(iris_df.describe())

# Check for missing values
print("\nCheck for missing values:")
print(iris_df.isnull().sum())

# Initialize the scaler
scaler = MinMaxScaler()

# Apply the scaler to the feature columns
iris_df[iris.feature_names] = scaler.fit_transform(iris_df[iris.feature_names])

# Display the transformed dataset
print("\nTransformed dataset (after Min-Max scaling):")
print(iris_df.head())

# One-hot encode the species column
iris_df = pd.get_dummies(iris_df, columns=['species'])

# Display the dataset with encoded categorical variables
print("\nDataset with one-hot encoded categorical variables:")
print(iris_df.head())

# Create a new feature 'petal_area'
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# Display the dataset with the new feature
print("\nDataset with the new feature 'petal_area':")
print(iris_df.head())
