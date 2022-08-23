import sys

lines = sys.stdin.readlines()    
lines = [line.strip() for line in lines]
line = "".join(lines)

for char in line:
    char = ord(char)
    c2 = char & 0b11111111   # low 8 bits
    char = char >> 8
    c1 = char & 0b11111111   # high 8 bits
    c1 = chr(c1)
    c2 = chr(c2)
    print(c1, end="")
    print(c2, end="")

print()
