import pandas as pd
import numpy as np

df = pd.read_csv("tiatanic.cs")

# How many of each value?

df["Sex"].value_counts()

df["Pclass"].value_counts()


# As proportions

df["Survived"].value_counts(normalize = True)


