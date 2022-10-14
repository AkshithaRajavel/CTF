#!/usr/bin/env python3

flag = #flag format uberctf{...}
key = open('/dev/urandom','rb').read(1)[0]
out = []
for c in flag:
    out.append(ord(c)^key)
    key = ord(c)
print(f'{bytes(out).hex() = }')

