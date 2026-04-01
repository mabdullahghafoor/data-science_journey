# In this program we will see some list methids

scores = [88, 76, 92, 65, 95, 76, 88, 100, 45]

# information methods

print(len(scores))
print(scores.count(76))
print(scores.index(92))
print(sum(scores))
print(max(scores))
print(min(scores))

# sorting methods

scores.sort()
print(scores)
print()

scores.sort(reverse = True)
print(scores)
print()

original= [25,10,69,100,58,33]
new_original = sorted(original)
print(original)
print(new_original)
print()

# Other useful methods
scores.reverse()
print(scores)

copy_1 = scores.copy()
print(copy_1)
print()