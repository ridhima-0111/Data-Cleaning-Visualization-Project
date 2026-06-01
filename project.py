import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("superstore.csv", encoding="latin1")

print("Original Shape:", df.shape)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Fill Missing Values
df = df.fillna(0)

# Save Cleaned Dataset
df.to_csv("cleaned_data.csv", index=False)

# Sales by Category
sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("sales_chart.png")

print("\nProject Completed Successfully!")
print("Files Generated:")
print("1. cleaned_data.csv")
print("2. sales_chart.png")

plt.show()