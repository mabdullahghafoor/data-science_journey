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


# ── Sort by frequency (highest first) ────────────────────────────
sorted_freq = dict(sorted(frequency.items(),
                          key=lambda x: x[1],
                          reverse=True))

print("\n📊 WORD FREQUENCY:")
print("─" * 25)
for word, count in sorted_freq.items():
    bar = "█" * count
    print(f"  {word:<10}: {bar} ({count})")

# Output:
# python    : ███ (3)
# is        : ███ (3)
# and       : ██ (2)
# great     : █ (1)
# easy      : █ (1)
# fun       : █ (1)


