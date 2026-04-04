# In this program we will see some example sof identity and membership operators

# Identity Operators

x = None
print(x is None)
print(x is not None)

a = [1,2,3]
b = [1,2,3]
c = a

print(a == b)
print(a is b)
print(a is c)
print()
# Membership Operators

name = "Fatima"
print("F" in name)
print("z" not in name)

grades = [85,90,78,92]
print(100 in grades)
print(90 in grades)