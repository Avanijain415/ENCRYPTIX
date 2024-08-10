import random
import string

def generate_password(length):
    password = ""
    all_characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(password_length):
        password += random.choice(all_characters)
    return password

while True:
    password_length = int(input("\nEnter the desired length of the password (at least 8 characters) : "))
    if password_length >= 8:
        break
    else:
        print("\nPassword length should be at least 8 characters. Please try again.")

pass_word = generate_password(password_length)
print("\nYour Generated Password : ",pass_word)