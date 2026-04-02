# In this program we will see some examples of 2d list

# ── 2D List = List of Lists = Matrix ────────────────────────────


# Each row is one student's marks across 3 subjects

gradebook = [
    ["Ali",    88, 76, 92],
    ["Sara",   45, 55, 38],
    ["Fatima", 95, 98, 100],
    ["Omar",   30, 42, 28],
]

print(gradebook[0])
print(gradebook[0][0])
print(gradebook[2][3])


# Loop through 2d list

print("\n Student Performance: ")
print("_" *35)

for row in gradebook:
    name = row[0]
    total = sum(row[1:])
    avg = total/3

    print(f"Name:{name:<10} Total:{total:<5} Average:{avg:<5}")