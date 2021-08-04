from Crypto.Cipher import AES
import os
def pad(a):
	size = (16-len(a)%16)%16
	a += chr(size)*size
	return a

iv = os.urandom(16)
key = os.urandom(16)
enc = AES.new(key,AES.MODE_CBC,iv)
print(iv.encode('hex'))


for _ in range(2):
	try:
		trick = raw_input("")
		trick = pad(trick.decode('hex'))
		cipher = enc.encrypt(trick)
		if trick == cipher and trick != "" :
			with open("flag.txt") as f:
				print(f.read())
				exit()
		else:
			print(cipher.encode('hex'))
			print("Try again")
	except:
		exit()