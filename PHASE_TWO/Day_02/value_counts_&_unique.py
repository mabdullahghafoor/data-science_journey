df["Pclass"].value_counts()


# As proportions

df["Survived"].value_counts(normalize = True)


# Unique values

df["Embarked"].unique()
df["Embarked"].nunique()


