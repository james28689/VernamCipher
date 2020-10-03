import string, random
from functions import xor

def vernam(plaintext, key):
	binary_plaintext = ["{0:08b}".format(ord(letter)).replace(" ", "") for letter in plaintext]
	binary_key = ["{0:08b}".format(ord(letter)).replace(" ", "") for letter in key]
	all_binary = [[binary_plaintext[i], binary_key[i]] for i in range(len(binary_plaintext))]
	binary_cipher = ["".join([str(xor(couple[0][x], couple[1][x])) for x in range(len(couple[0]))]) for couple in all_binary]
	plaintext_cipher = "".join([chr(int(letter, 2)) for letter in binary_cipher])

	return(plaintext_cipher)

plaintext = input("Original Text: ")
key = [random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(len(plaintext))]

ciphertext = vernam(plaintext, key)
print(ciphertext)
print([letter for letter in ciphertext])
print("".join(key))
print(vernam(ciphertext, key))