# In This Program we will see how to use variable scope

# ── Scope = where a variable EXISTS and can be used ──────────────

name = "Ali"        # GLOBAL variable — exists everywhere

def show_name():
    name = "Sara"   # LOCAL variable — only exists inside function
    print(name)     # Sara (local wins inside function)

show_name()         # Sara
print(name)         # Ali (global unchanged!)