# Using np.where for a simple binary label

df["Adult"] = np.where(df["Age"] >= 18 , "Yes" , "No")
