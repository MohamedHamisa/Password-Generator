import string
import random
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_numbers = input("How many characters do you want?")
while True:
  try:
    characters_numbers = int(characters_numbers)
    if characters_numbers < 6:
      print("You need at least 6 ")
      characters_numbers = input("Enter the number again?")
    else:
      break
  except:
    print("Enter numbers only")
    characters_numbers = input("Enter the number again for password?")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1= round(characters_numbers*0.3)
part2= round(characters_numbers*0.2)

password = []

for i in range(part1):
  password.append(s1[i])
  password.append(s2[i])

for i in range(part2):
  password.append(s3[i])
  password.append(s4[i])

random.shuffle(password)
password ="".join(password[0:])

print(password)


