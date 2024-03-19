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

def decode(encoded_code):
    string = ""
    for i in encoded_code:
        j = int(i) - 3
        if j < 0:
            j = str(j)
            j = j[1]
        string += str(j)
    return string





def main():
    while True:
        option = input("Choose an option: ")
        print("1. encode")
        print("2. decode")


