# In this program we will see a real world problem eample in python

# ── This exact pattern is used in NLP & Text Analysis ────────────
text = "python is great and python is easy and python is fun"

words     = text.split()    # split sentence into list of words
frequency = {}              # empty dictionary to store counts

for word in words:
    if word in frequency:
        frequency[word] += 1    # word seen before → increment
    else:
        frequency[word] = 1     # first time seeing word → set to 1

print(frequency)