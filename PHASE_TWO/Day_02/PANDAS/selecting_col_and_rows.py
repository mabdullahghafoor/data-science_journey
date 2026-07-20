import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

# --- SELECTING COLUMNS ---


# Single column → returns a Series

df.Age  # Whe co;l name has space dont use rhis use brackets
df["Age"]

# Multiple columns → returns a DataFrame

df[["Name" , "Age" , "Survived"]]



# --- SELECTING ROWS: .loc and .iloc ---


# .loc  → label-based (use index labels and column names)

df.loc[0]  # 1st row

df.loc[0 , "Name"] # 1st roc and name col

df.loc[0:4 , "Name" : "Age"] # ros 0 - 4 and col name through age [Inclusive]

df.loc[df["Age"] > 30 , "Name"] # Rows where age >30 only name col



