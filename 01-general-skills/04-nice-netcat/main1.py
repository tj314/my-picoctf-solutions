import sys

for line in sys.stdin:
    line = line.strip()
    c = chr(int(line))
    print(f"{c}", end="")
print()
