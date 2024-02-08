'''
Converts text to base64 and base64 to plaintext
can make a file or use a file u got already to store
the results, it also prints the results in the terminal
the program can also take input from a hex file and covert it to ascii
'''
import argparse
from time import sleep
import sys
import base64
from cowsay import trex

conv = ""
command = ""

def command():
    command = input("""
quit - quits the program
b64 - pulls up the base64 converter
hex - pulls up the hex converter
""")
    if command == "quit":
        sys.exit()
    elif command == "b64":
        menu()
    elif command == "hex":
        get_results()
    else:
        test = "wtf was that? it wasnt one of the commands lol"
        print(trex(test))



def menu():
    string = input('''
What you trynna do? Encrypt or Decrypt?
encrypt:(e):
decrypt:(d):
quit:(q):

/> ''')
    if string == "e":
        string_to_bytes(conv)
    elif string == "d":
        bytes_to_string(conv)
    elif string == "q":
        print("Ight im out")
    else:
        print("Not sure what u mean, try again")
        menu()


def string_to_bytes(conv):
    b64_file = input("Name a file or choose a file you have?/> ")
    test_e = input("Lemme get dat txt: ")
    conv = test_e.encode('utf-8')
    b64_e = base64.b64encode(conv)
    print(f"This is whats gonna be in the file: {b64_e}")
    with open(b64_file, 'w') as b64_file:
        b64_file.write(f"Decoded Base64:  {b64_e}")
    menu()

def bytes_to_string(conv):
    b64_file = input("Name a file or choose a file you have?/> ")
    text_d = input("Lemme see dat b64: ")
    conv = text_d.encode('utf-8')
    b64_d = base64.b64decode(conv)
    print(f"This is whats gonna be in the file: {b64_d}")
    with open(b64_d, 'w') as b64_file:
        b64_file.write(f"Decoded Base64: {b64_d}")
    print(b64_d)
    menu()



def generate_mapping(hex_value, decimal_value):
    binary_value = format(decimal_value, '08b')
    ascii_char = chr(decimal_value) if 32 <= decimal_value <= 126 else 'N/A'
    return f"{hex_value}\t{decimal_value}\t{binary_value}\t{ascii_char}"



def get_results():
    generated_mappings = [generate_mapping(f"{i:02X}", i) for i in range(128)]

    generated_mappings.append("I cant find a damn thing else! Im outta here.")

    with open(input("What is the name of the hex file?:/> ")) as f:
        line = f.readline().strip()

    print("Hex\tDecimal\tBinary\t\tCharacter\n")
    i = 0
    i2 = 3
    while True:
        hex_segment = line[i:i2]
        if hex_segment:
            print(generated_mappings[int(hex_segment, 16)])
            i += 3
            i2 += 3
        else:
            command()


command()
