# Hei Man Cheung encoder and main function
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # Shift each digit by 3, wrap around using % 10
        encoded_password += encoded_digit
    return encoded_password


# Main function to display menu and handle user inputs
def main():
    encoded_password = ""  # To store the encoded password

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            # Encoding option
            password = input("Please enter your password to encode: ")

            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid input. Please enter an 8-digit password consisting only of numbers.")


        elif option == "3":
            # Quit option
            break


if __name__ == "__main__":
    main()
