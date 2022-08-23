import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]
    for pos in pos_pw_list:
        user_pw_hash = hash_pw(pos)
    
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            print(f"The password was {pos}.")
            decryption = str_xor(flag_enc.decode(), pos)
            print(decryption)
            return


level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)

