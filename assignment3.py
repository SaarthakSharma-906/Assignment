import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Display the first few rows of the dataset
print(iris.head())

# Pairplot
sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
plt.suptitle('Pairwise Relationships in Iris Dataset', y=1.02)
plt.show()

# Distribution plots for each feature
plt.figure(figsize=(12, 8))
for i, feature in enumerate(iris.columns[:-1]):
    plt.subplot(2, 2, i+1)
    sns.histplot(iris[feature], kde=True)
    plt.title(f'Distribution of {feature}')
plt.tight_layout()
plt.show()

# Boxplots to see the distribution of features per species
plt.figure(figsize=(12, 8))
for i, feature in enumerate(iris.columns[:-1]):
    plt.subplot(2, 2, i+1)
    sns.boxplot(x="species", y=feature, data=iris)
    plt.title(f'Boxplot of {feature} by Species')
plt.tight_layout()
plt.show()
