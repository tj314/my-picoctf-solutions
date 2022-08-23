import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

flag = "".join([chr(int(line.strip())) for line in lines])
print(flag)
