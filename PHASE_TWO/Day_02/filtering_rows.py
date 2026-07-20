# Combine filter + column selection
df[df["Survived"] == 1][["Name" , "Age" , "Pclass"]]

# or equivalently:
df.loc[df["Survived"] == 1 , ["Name" , "Age" , "Pclass"]]

