df[df["Survived"] == 1]


# Multiple conditions — use & (and), | (or), ~ (not)
# IMPORTANT: each condition must be wrapped in parentheses

df[(df["Age"] > 30) & (df["Sex"] == "female")]

df[(df["Pclass"] == 1) | (df["Pclass"] == 2)]

df[~(df["Embarked"] == "S")]

# .isin() — cleaner way to filter multiple values
df[df["Pclass"].isin([1,2])]

# .between() — range filter
df[df["Age"].between(30,40)]


# Combine filter + column selection
df[df["Survived"] == 1][["Name" , "Age" , "Pclass"]]

# or equivalently:
df.loc[df["Survived"] == 1 , ["Name" , "Age" , "Pclass"]]

