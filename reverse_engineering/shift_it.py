import string
import random

flag = #format : "uberctf{...}"
mystery_num = random.randint(100,1000)
new_alphabet = list(string.ascii_lowercase + string.digits + string.punctuation)
enc_flag = ""

def shift(char):
  index = new_alphabet.index(char)
  new_index = (index + mystery_num) % len(new_alphabet)
  return new_alphabet[new_index]

for char in flag:
  enc_flag += shift(char)
  mystery_num += 10

print(enc_flag)