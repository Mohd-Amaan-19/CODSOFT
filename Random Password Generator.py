import random
import string
alphabets = string.ascii_letters
numbers = string.digits
less_ch = '#$%'
characters = '!~@#$%^&*(_+|?><|)'
total = ""
def generate_password(level, length):
    if level == "easy":
        total = alphabets + numbers
        password =  ''.join(random.choice(total) for _ in range(length))
        return password
    elif level == "medium":
        total = alphabets + numbers + less_ch
        password =  ''.join(random.choice(total) for _ in range(length))
        return password
        
    elif level == "hard":
        total = alphabets + numbers + characters
        password =  ''.join(random.choice(total) for _ in range(length))
        return password
        
    else:
        return "Invalid Choice"
        
print("\t\t\t RANDOM PASSWORD GENERATOR\n")
try:        
    length = int(input("Enter desired length of Password(min=4 , max=21):\n"))
    while(length not in range(4,21)):
        print("Enter Correct Length\n ")
        length = int(input("Enter Length Again: "))
except:
    print("Your Input is Invalid\n")
    exit()
list2 = ['easy', 'medium','hard']
level = input("Enter Difficulty level ('easy', 'medium','hard'):\n").lower()
while(level not in list2):
    print("Invalid Input")
    level = input("Please Enter Difficulty level ('easy', 'medium','hard'):\n").lower()
        

password = generate_password(level,length)
print(f"Your Generated Password is: {password}\n")
print("Thanks for Using Random Password Generator!!")
    