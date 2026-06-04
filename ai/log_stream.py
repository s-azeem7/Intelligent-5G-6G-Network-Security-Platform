import time
from engine import detect

LOG_FILE = "/root/5g-security-platform/logs/amf.log"

print("AI LOG MONITOR STARTED...")

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(1)
            continue
        yield line

with open(LOG_FILE, "r") as f:
    for line in follow(f):
        result = detect(line)
        print(f"{result} | {line.strip()}")
