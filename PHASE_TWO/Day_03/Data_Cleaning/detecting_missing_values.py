import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

# Count of nulls per column

a = df.isnull().sum()
print(a)
print()
# Percentage of Missing Values For More Useful Decision

b = ((df.isnull().sum() / len(df) ) * 100).round(2)
print(b)
print()

# Whiich row has at least one null

