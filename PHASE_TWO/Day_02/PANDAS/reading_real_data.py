import pandas as pd

import numpy as np


# Read a CSV file

df = pd.read_csv("titanic.csv")


# Read from a URL directly (useful in Colab/Kaggle)

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)


# Other formats

