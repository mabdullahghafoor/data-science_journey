#In this program we will see how to append and write a file

# ── "w" mode — DANGEROUS if file exists ──────────────────────────

with open("log.txt", "w") as file:

    file.write("Entry 1\n")


with open("log.txt", "w") as file:
    file.write("Entry 2\n") # ❌ First entry is GONE!

# ── "a" mode — SAFE, adds to end ─────────────────────────────────

with open("log.txt", "a" ) as file:
    file.write("Entry 1\n")

with open("log.txt", "a") as file:
    file.write("Entry 2\n") # ✅ Entry 1 still there!

with open("log.txt", "a") as file:
    file.write("Entry 3\n") # ✅ Both entries still there!

# File now contains:
# Entry 1
# Entry 2
# Entry 3


# ── Real world: activity logger ───────────────────────────────────

from datetime import datetime

def log_activity(action):
    # Append a timestamped activity to a file

    timestamped = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("login.txt", "a") as file:
        file.write(f"[{timestamped}] {action}\n")

log_activity("User Ali Logged In!")
log_activity("User Ali view Dashboard!")
log_activity("User Ali Logged Out!")

