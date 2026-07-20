df.loc[0]  # 1st row

df.loc[0 , "Name"] # 1st roc and name col

df.loc[0:4 , "Name" : "Age"] # ros 0 - 4 and col name through age [Inclusive]

df.loc[df["Age"] > 30 , "Name"] # Rows where age >30 only name col



# .iloc → position-based (use integer positions, like NumPy)

df.iloc[0] # 1st row

df.iloc[0 , 2] # 1st eow and col at position 2

df.iloc[0:5 , 0:3] # first 5 rows and first 3 col

df.iloc[-1] # last row


#The .loc vs .iloc distinction matters. Remember it this way:

# .loc → label → you use the actual name
# .iloc → integer → you use the position number
