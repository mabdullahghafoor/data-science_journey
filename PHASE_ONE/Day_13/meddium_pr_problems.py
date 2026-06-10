# In this we will solve some medium level problems

# This problems contains some extra files and their names are listed below

# 1. string_utils.py
# 2. main.py
# 3. random_data_generator.py
# 4. main2.py

from collections import Counter

# Character frequency
text = "hello world"
char_count = Counter(text)

print("Character frequency:")
print(char_count)

# Top 3 most common marks
marks = [80, 75, 90, 80, 85, 90, 90, 75, 80, 95]

mark_count = Counter(marks)
