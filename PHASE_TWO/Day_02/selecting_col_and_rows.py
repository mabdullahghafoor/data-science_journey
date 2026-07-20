# .iloc → position-based (use integer positions, like NumPy)

df.iloc[0] # 1st row

df.iloc[0 , 2] # 1st eow and col at position 2

df.iloc[0:5 , 0:3] # first 5 rows and first 3 col

df.iloc[-1] # last row


#The .loc vs .iloc distinction matters. Remember it this way:

# .loc → label → you use the actual name
# .iloc → integer → you use the position number
