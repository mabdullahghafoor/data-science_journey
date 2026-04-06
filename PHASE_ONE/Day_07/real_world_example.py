# In this program we will see some subsets and supersets


# ── Scenario: Clean a messy dataset ─────────────────────────────
# Imagine these are user IDs from two different data sources
source_A = [101, 102, 103, 104, 102, 101, 105]   # has duplicates
source_B = [103, 104, 106, 107, 103, 108]          # has duplicates


# Step 1: Remove duplicates from each source

clean_A = set(source_A)
clean_B = set(source_B)

print(clean_A)
print(clean_B)


# Step 2: Find users in BOTH sources (already registered)

both = clean_A & clean_B
print(f"Common Data Values are : {both}")


# Step 3: Find NEW users only in source B

user_B = clean_B - clean_A
print(f"Unique user in B are : {user_B}")


# Step 4: All unique users combined
unique = clean_A | clean_B
print(f"All unique users : {unique}")