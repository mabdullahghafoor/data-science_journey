import pandas as pd
import numpy as np

df = pd.read_csv("tiatanic.cs")

# Single condition

df[df["Age"] > 30]

