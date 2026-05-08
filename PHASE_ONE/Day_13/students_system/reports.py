# In this we will see how to create our own package

# FILE: reports.py
from datetime import datetime

def generate_report_header(title):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'═'*45}")
    print(f"  {title}")
    print(f"  Generated: {timestamp}")
    print(f"{'═'*45}")