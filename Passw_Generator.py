import random
import string
def Generate_passw(length=12):
    if length<4:
        return "Password is too short"
    string.ascii_letters
    string.digits
    string.punctuation
    all_chars=string.ascii_letters+string.digits+string.punctuation
    pass_word=random.choices(all_chars,k=length)
    return pass_word
    
try:
    length=int(input("Enter length of password:(min:4)\n"))
    print(Generate_passw(length))
except ValueError:
    print("OOps! something went wrong,Try again")
