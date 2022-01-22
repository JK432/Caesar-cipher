#Write a program to implement Caser cipher (input a line of plain text and distance value and outputs an encrypted text)
plaintext = input()
shift = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""
while isinstance(int(shift), int) == False:
  shift = input("")
shift = int(shift)
new_ind = 0 
for i in plaintext:
  if i.lower() in alphabet:
    new_ind = alphabet.index(i) + shift
    ciphertext += alphabet[new_ind % 26]
  else:
    ciphertext += i    
print(ciphertext)
    