import pandas as pd
import numpy as np

df = pd.read_csv("tiatanic.cs")

# Single condition

df[df["Age"] > 30]

df[df["Sex"] == "female"]

df[df["Survived"] == 1]


# Multiple conditions — use & (and), | (or), ~ (not)
# IMPORTANT: each condition must be wrapped in parentheses

df[(df["Age"] > 30) & (df["Sex"] == "female")]

df[(df["Pclass"] == 1) | (df["Pclass"] == 2)]

df[~(df["Embarked"] == "S")]

