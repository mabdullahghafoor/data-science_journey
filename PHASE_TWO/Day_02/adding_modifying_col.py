import pandas as pd
import numpy as np

df = pd.read_csv("tiatanic.cs")

# Add a new column

df["FamilySize"] = df["Sibsp"] + df["Parch"] + 1


# Modify an existing column

df["Fare"] = df["Fare"].round(2)



# Create a column based on a condition

