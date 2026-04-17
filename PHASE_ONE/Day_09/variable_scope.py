# In This Program we will see how to use variable scope

# ── Scope = where a variable EXISTS and can be used ──────────────

name = "Ali"        # GLOBAL variable — exists everywhere

def show_name():
    name = "Sara"   # LOCAL variable — only exists inside function
    print(name)     # Sara (local wins inside function)

show_name()         # Sara
print(name)         # Ali (global unchanged!)

# ── global keyword — modify global variable inside function ───────
counter = 0         # global

def increment():
    global counter  # tell Python: use the GLOBAL counter
    counter += 1

increment()
increment()
increment()
print(counter)      # 3

# ── Rule of thumb ────────────────────────────────────────────────
# ✅ Read global variables inside functions — fine
# ⚠️ Modify global variables inside functions — use sparingly
# ✅ Best practice: pass values IN via parameters,
#                                   get values OUT via return