def CipherText(plaintext,shift):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext=""
    new_ind=0
    for i in plaintext:
      if(i in alphabet):
        new_ind=alphabet.index(i)+shift
        ciphertext+=alphabet[new_ind % 26]   #(plus)
      elif(i in ALPHABET):
          new_ind=ALPHABET.index(i)+shift
          ciphertext+=ALPHABET[new_ind % 26]
      else:
        ciphertext+=i    #(this statement is for adding space)
    return ciphertext
plaintext=input("Please enter your plaintext: ")  #(minus)
shift=int(input("Please enter your key: "))
cip=CipherText(plaintext,shift)
print("The cipher text is:",cip)