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
        shifted = (ord(char) - ord('a') + shift)%26 + ord('a')
        return chr(shifted)
    else:
        return char 
    
def encrypt(message , shift):
    encrypt_message = ''
    for char in message:
        encrypt_message += shift_character(char , shift)
    return encrypt_message

def decrypt (message , shift):
    decrypt_message = ''
    for chr in message:
        decrypt_message += shift_character(chr , -shift)
    return decrypt_message
    
def display_result (result , action):
    print(f"the {action}ed message is :{result}")

def main():
    while True:
        choice = display_menu()

        if choice == '1':
            message , shift = get_inputs()
            encrypt_message = encrypt(message,shift)
            display_result(encrypt_message , "encrypt")
        elif choice == '2':
            message ,shift = get_inputs()
            decrypt_message = decrypt(message,shift)
            display_result(decrypt_message , "decrypt")
        elif choice == '3':
            print('Goodbye!!!')
            break
main()
