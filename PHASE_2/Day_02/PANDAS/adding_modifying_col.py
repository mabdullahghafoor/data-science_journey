import pandas as pd
import numpy as np

df = pd.read_csv("tiatanic.cs")

# Add a new column

df["FamilySize"] = df["Sibsp"] + df["Parch"] + 1


# Modify an existing column

df["Fare"] = df["Fare"].round(2)



# Create a column based on a condition

df["AgeGroup"] = pd.cut(df["Age"] , bins = [0 , 18 , 40 , 60] ,
                        labels = ["Child" , "Adult" , "Senior"])


# Using np.where for a simple binary label

df["Adult"] = np.where(df["Age"] >= 18 , "Yes" , "No")
