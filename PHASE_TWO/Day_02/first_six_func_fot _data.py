import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

df.head() # For first 5 rows

df.tail(3) # For lat 3 rows
 
df.shape # No of rows and col

df.info() # for no f col, data types and Non Null values

df.describe() # Summary for each col like mean, std , var

