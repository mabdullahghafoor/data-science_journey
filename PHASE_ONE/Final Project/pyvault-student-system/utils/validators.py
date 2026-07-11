# ═══════════════════════════════════════════════════
def get_float(prompt, min_val=None, max_val=None):
    while True:
            value = float(input(prompt).strip())
            if min_val is not None and value < min_val:
