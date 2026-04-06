# In this program we will see some subsets and supersets

# ── Is one group INSIDE another? ────────────────────────────────
admins    = {"Ali", "Sara"}
all_staff = {"Ali", "Sara", "Fatima", "Omar", "Zara"}


# Subset → is admins completely inside all_staff?
print(admins.issubset(all_staff))       # True  ✅
print(admins <= all_staff)              # True  (same thing)

