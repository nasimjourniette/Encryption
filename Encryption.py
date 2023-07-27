# here we go...
import math
def main():
    while True:
        try:
            choice = input("Type encode to encrypt or type decode to decrypt\n").lower()
            if choice not in ('encode', 'decode'):
                raise ValueError
        except ValueError:
            print("Please type in either encode or decode.")
        else:
            message = input('Type your message:\n')
            while True:
                try:
                    displacement = int(input('By how much would you like to displace this message?\n'))
                except ValueError:
                    print('Please input an integer.')
                else:
                    break
            print(caesar(choice, message, displacement))
            break        
    
    go_again(main)
    

def go_again(func):
    while True:
        again = input("Would you like to go again? Type 'yes' or 'no'\n").lower()
        if again == 'yes':
            func()
            break
        elif again == 'no':
            quit()
        else:
            pass    


def caesar(type, message, displacement):
    new_message = []
    loop = math.ceil(displacement/26)
    for char in message:
        if not char.isalpha():
            new_message.append(char)
        else:
            if type == 'encode':
                new_char = chr(ord(char) + displacement)
                if ord(new_char) > 122 and char.islower():
                    new_char = chr(ord(new_char) - 26*loop)
                elif ord(new_char) > 90 and char.isupper():
                    new_char = chr(ord(new_char) - 26*loop)
                new_message.append(new_char)
            elif type == 'decode':
                new_char = chr(ord(char) - displacement)
                if ord(new_char) < 97 and char.islower():
                    new_char = chr(ord(new_char) + 26*loop)
                elif ord(new_char) < 65 and char.isupper():
                    new_char = chr(ord(new_char) + 26*loop)
                new_message.append(new_char)
    return ''.join(new_message)
    

if __name__ == "__main__":
    main()

