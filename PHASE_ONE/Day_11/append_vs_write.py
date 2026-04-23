#In this program we will see how to append and write a file

# ── "w" mode — DANGEROUS if file exists ──────────────────────────

with open("log.txt", "w") as file:

    file.write("Entry 1\n")


with open("log.txt", "w") as file:
    file.write("Entry 2\n") # ❌ First entry is GONE!

