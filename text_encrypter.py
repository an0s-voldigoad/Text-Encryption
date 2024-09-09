def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def print_success(message):
    print("\033[92m" + message + "\033[0m")  # Green text

def print_failure(message):
    print("\033[91m" + message + "\033[0m")  # Red text

def print_logo():
    logo = """
\033[91m
___ ____ _  _ ___    ____ _  _ ____ ____ _   _ ___  ___ ____ ____ 
 |  |___  \/   |     |___ |\ | |    |__/  \_/  |__]  |  |  | |__/ 
 |  |___ _/\_  |     |___ | \| |___ |  \   |   |     |  |__| |  \ 
                                                                  

                       ~       BY MISFIT KING         ~
   \033[0m
"""
    print(logo)

def main():
    print_logo()
    
    while True:
        print("Welcome to the Text Encryption Tool!")
        print("\nMain Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        option = input("Choose an option (1/2/3): ").strip()
        
        if option == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift amount (integer): "))
            encrypted_text = encrypt(text, shift)
            print_success("Encrypted text: " + encrypted_text)
        
        elif option == '2':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift amount (integer): "))
            decrypted_text = decrypt(text, shift)
            print_success("Decrypted text: " + decrypted_text)
        
        elif option == '3':
            print("Exiting...")
            break
        
        else:
            print_failure("Invalid option selected. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
