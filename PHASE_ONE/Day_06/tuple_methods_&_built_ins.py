# In this program we will some some examples to about tuples methods and builts in

# ── Tuples only have 2 methods (unlike list's many) ─────────────
scores = (88, 76, 92, 76, 65, 92, 88)

print(scores.count(76))     # 2   → how many times 76 appears
print(scores.index(92))     # 2   → index of FIRST 92
print(len(scores))          # 7   → total items
print(min(scores))          # 65  → minimum
print(max(scores))          # 92  → maximum
print(sum(scores))          # 577 → total

# ── Loop through tuple — same as list ───────────────────────────
for score in scores:
    print(score)

# ── Check membership ────────────────────────────────────────────
print(92 in scores)         # True
print(100 in scores)        # False