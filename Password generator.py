import random
import string


def Generate():
    try:
        character=int(input("Enter Length:- "))
        if character<=0:
            print("Length must be greater than 0")
            return
    except Exception as ex:
        print("Give integer type value only")
        return
    characters=string.ascii_letters+string.punctuation+string.digits
    password=""
    for i in range(character):
        password+=random.choice(characters)
    print(password)
    

def Checker():
        password=input("Enter your password:- ")
        has_upper=False
        has_lower=False
        has_digit=False
        has_special=False
        for i in password:
            if i in string.ascii_uppercase:
                has_upper=True
            if i in string.ascii_lowercase:
                has_lower=True
            if i in string.digits:
                has_digit=True
            if i in string.punctuation:
                has_special=True
        score = 0
        if has_upper:
            print("Uppercase yess")
            score+=1
        if has_lower:
            print("lowercase yess")
            score+=1
        if has_digit:
            print("Numbers yess")
            score+=1
        if has_special:
            print("Special symbol yess")
            score+=1
        if len(password)>=8:
            print("Length is perfect ")
            score+=1

        if score == 5:
            print("Strong")
        elif score>=3:
            print("Medium")
        else:
            print("Weak")
    

while True:
        try:
            print("\nWelocome to password generator")
            print("Generate password    - Click 1")
            print("Strength cheacker    - Click 2")
            print("Exit                 - Click 3")
            choice=int(input("Enter your choice:- "))
        
            if choice == 1:
                Generate()
            elif choice == 2:
                Checker()
            elif choice == 3:
                break
            else:
                print("Invalid coice")
        except Exception as ex:
            print("Give only 1,2 or 3")  