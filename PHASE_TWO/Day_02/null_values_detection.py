import pandas as pd
import numpy as np

df = pd.read_csv("tiatanic.cs")


df.isnull().sum()

df.isnull().sum() / len(df) * 100

# Which rows have any null?

