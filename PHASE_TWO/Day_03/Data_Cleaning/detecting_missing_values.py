import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

# Count of nulls per column

# Count of nulls per column
df.isnull().sum()
# PassengerId      0
# Survived         0
# Pclass           0
# Name             0
# Sex              0
# Age            177   ← 177 missing
# SibSp            0
# Parch            0
# Ticket           0
# Fare             0
# Cabin          687   ← 687 missing (77% of data!)
# Embarked         2   ← only 2 missing

# Percentage missing — more useful for decisions
(df.isnull().sum() / len(df) * 100).round(2)

# Which rows have at least one null?
df[df.isnull().any(axis=1)].head()

# How many rows are completely clean?
