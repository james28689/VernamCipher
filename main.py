import string, random

def xor(a, b):
	if a != b:
		return(1)
	else:
		return(0)

def vernam(plaintext, key):

	binary_plaintext = ""
	for letter in plaintext:
		binary_plaintext += "{0:08b}".format(ord(letter))
	binary_plaintext.replace(" ", "")

	binary_key = ""
	for letter in key:
		binary_key += "{0:08b}".format(ord(letter))
	binary_key.replace(" ", "")

	binary_cipher = ""
	for i in range(len(binary_plaintext)):
		binary_cipher += str(xor(binary_plaintext[i], binary_key[i]))

	plaintext_cipher = ""
	for i in range(0, len(binary_cipher), 8):
		plaintext_cipher += chr(int(binary_cipher[i:i+8], 2))
	
	return(plaintext_cipher)

plaintext = input("Original Text: ")
key = [random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(len(plaintext))]

ciphertext = vernam(plaintext, key)
print(ciphertext)
print([letter for letter in ciphertext])
print("".join(key))
print(vernam(ciphertext, key))