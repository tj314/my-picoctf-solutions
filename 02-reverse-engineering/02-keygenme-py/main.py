import hashlib

username_trial = b"ANDERSON"
d = hashlib.sha256(username_trial).hexdigest()
s = d[4] + d[5] + d[3] + d[6] + d[2] + d[7] + d[1] + d[8]
print(s)
