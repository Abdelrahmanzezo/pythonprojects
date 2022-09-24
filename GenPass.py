import string
import random
s1 = list(string.ascii_letters)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
number_charcters = input("How many numbers of Charcters do you need for your password?!....")
while True:
    try:
        number_charcters=int(number_charcters)
        if number_charcters < 6:
            print("you need at least 6 numbers")
            number_charcters=input("please enter the number of characters again")
        else:
            break
    except:
        print("please enter numbers only")
        number_charcters=input("How many numbers of Charcters do you need for your password?!....")
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
part1 = round(number_charcters*(30/100))
part2 = round(number_charcters*(20/100))
password = []
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
random.shuffle(password)
password = "".join(password[0:])
print(f"the Generator password is ->>>> {password}")
