def display_menu():
    print("Welcome to the Caesar Cipher Program!")
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input(" Enter your choice (1, 2, or 3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter your choice (1, 2, or 3): ")

    return choice

def get_inputs ():
    message = input('Please enter a message : ')
    while True:
        try:
            shift = int(input("Enter a shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return message , shift


def shift_character(char , shift):
    if char.isupper():
        shifted = (ord(char) - ord('A') + shift)%26 + ord('A')
        return chr(shifted)
    elif char.islower():
        shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
        return chr(shifted)
    else:
        return char 
    
def encrypt(message , shift):
    encrypt_message = ''
    for char in encrypt_message:
        encrypt_message += shift_character(char , shift)
    return encrypt_message

def decrypt (message , shift):
    decrypt_message = ''
    for chr in message:
        decrypt_message += shift_character(message , -shift)
    return decrypt_message
    
