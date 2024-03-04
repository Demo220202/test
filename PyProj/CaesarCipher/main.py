alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art

print(art.logo)

def caesar(text, shift, direction) :

  end_text = ""
  
  if direction == "decode" :
    shift *= -1;
  
  for char in text :
    if char in alphabet :
      pos = alphabet.index(char)
      pos = pos + shift
      end_text += alphabet[pos]
    else :
      end_text += char
  
  print(f"The {direction}d text is : {end_text}")

user_choice = "yes"
while user_choice != "no" :
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(text, shift, direction)
  user_choice = input("Want to encode or decode again ? ")

  if user_choice == "no" :
    print("GoodBye!")
