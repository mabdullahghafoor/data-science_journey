# In this program we will see some examples of list unpacking and advanced list

# ── Unpacking: assign list items to variables ────────────────────
first, second, third = [10,20,30]
print(first,second,third)


# ── Extended unpacking ───────────────────────────────────────────
first, *middle, last = [10,20,30,40,50]
print(first, middle, last)


# ── Check membership ────────────────────────────────────────────
fruits = ["apple", "mango", "banana", "cherry"]
print("mango" in fruits)
print("grape" not in fruits)


# ── Concatenate & repeat ─────────────────────────────────────────
list1 = [1,2,3]
list2 = [4,5,6]

print(list1 + list2)
print(list1 * 3) 