# From a dictionary — most common way

import pandas as pd
import numpy as np

data = {
    "name":   ["Ali", "Sara", "Ahmed", "Zara"],
    "age":    [23, 27, 22, 25],
    "city":   ["Karachi", "Lahore", "Karachi", "Islamabad"],
    "salary": [45000, 62000, 38000, 71000]
}

df = pd.DataFrame(data)

print(df)
print()
