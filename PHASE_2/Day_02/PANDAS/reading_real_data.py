import pandas as pd

import numpy as np


# Read a CSV file

df = pd.read_csv("titanic.csv")


# Read from a URL directly (useful in Colab/Kaggle)

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)


# Other formats

df = pd.read_excel("data.xlsx")

df = pd.read_json("data.json")

# Useful parameters

df = pd.read_csv("data.csv" , nrows = 100)
df = pd.read_csv("data.csv" , usecols = ["name" , "age"])
df = pd.read_csv("data.csv" , index_col = "id")

