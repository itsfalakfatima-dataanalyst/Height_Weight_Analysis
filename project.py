import pandas as pd
data = pd.read_csv(r"c:\Users\ABCD\Downloads\hw_200.csv")

import pandas as pd

# Load CSV
data = pd.read_csv(r"c:\Users\ABCD\Downloads\hw_200.csv")

# Clean column names
data.columns = ['Index', 'Height', 'Weight']

# Display first and last rows
print("First 5 rows:")
print(data.head())
print("\nLast 5 rows:")
print(data.tail())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Detect outliers using IQR
Q1 = data['Weight'].quantile(0.25)
Q3 = data['Weight'].quantile(0.75)
IQR = Q3 - Q1
outliers = data[(data['Weight'] < Q1 - 1.5*IQR) | (data['Weight'] > Q3 + 1.5*IQR)]
print("\nOutliers in Weight:")
print(outliers)

# Save cleaned data
data.to_csv("hw_200_cleaned.csv", index=False)
print("\nCleaned data saved as hw_200_cleaned.csv")





import pandas as pd

# Load CSV
data = pd.read_csv(r"c:\Users\ABCD\Downloads\hw_200.csv")
data.columns = ['Index', 'Height', 'Weight']

# Create height categories
data['Height_Category'] = pd.cut(data['Height'], bins=[60, 65, 70, 75], labels=['Short', 'Medium', 'Tall'])

# Value counts for categories
print("Height Categories Count:")
print(data['Height_Category'].value_counts())

# Aggregation: mean, min, max per category
height_group = data.groupby('Height_Category')['Weight'].agg(['mean', 'min', 'max'])
print("\nWeight Stats by Height Category:")
print(height_group)

# Sort by weight descending
sorted_data = data.sort_values(by='Weight', ascending=False)
print("\nTop 5 Heaviest People:")
print(sorted_data.head())

# Export grouped data
height_group.to_csv("height_weight_summary.csv")
print("\nGrouped summary saved as height_weight_summary.csv")


height_group = data.groupby('Height_Category', observed=True)['Weight'].agg(['mean', 'min', 'max'])





