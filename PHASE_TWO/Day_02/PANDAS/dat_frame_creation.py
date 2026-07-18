    "age":    [23, 27, 22, 25],
    "city":   ["Karachi", "Lahore", "Karachi", "Islamabad"],
    "salary": [45000, 62000, 38000, 71000]
}

df = pd.DataFrame(data)
print(df)
#     name  age       city  salary
# 0    Ali   23    Karachi   45000
# 1   Sara   27     Lahore   62000
# 2  Ahmed   22    Karachi   38000
# 3   Zara   25  Islamabad   71000

# Key attributes
print(df.shape)    # (4, 4) — 4 rows, 4 columns
print(df.columns)  # Index(['name', 'age', 'city', 'salary'])
print(df.dtypes)   # name: object, age: int64, city: object, salary: int64
print(df.index)    # RangeIndex(start=0, stop=4, step=1)