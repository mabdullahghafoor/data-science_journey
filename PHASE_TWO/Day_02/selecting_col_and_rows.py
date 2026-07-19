import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

# --- SELECTING COLUMNS ---


# Single column → returns a Series

df.Age  # Whe co;l name has space dont use rhis use brackets
df["Age"]

