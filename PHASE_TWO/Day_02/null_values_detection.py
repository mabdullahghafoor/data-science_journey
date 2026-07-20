# Which rows have any null?

df[df.isnull().any(axis=1)]


# Is a specific value null?
df["Age"].isnull()