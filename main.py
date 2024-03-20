#Colgan Miller project code

def encode(code):
    string = ''
    for i in code:
        j = int(i)+3
        if j >= 10:
            j = str(j)
            j = j[1]

        string += str(j)

    return string






def main():
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
            encode_num = encode(password)
        elif option == 2:
            encode_num = encode(password)
            print(f"The encoded password is {encode_num}, and the original password is {password}.")
        elif option == 3:
            break

if __name__ == "__main__":
    main()

