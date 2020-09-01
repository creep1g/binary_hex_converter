import math
def ToBinary(int):
    bits = []
    counter = 7
    dec = int
    #TODO: break bytes into 4 bit sections
    if dec > 255:
        dec_temp = dec
        controller = False
        while controller == False:
            dec_temp -= 255
            if dec_temp <=255 and dec_temp >= 1:
                counter += 7
            elif dec_temp > 255:
                if dec_temp < 510:
                    counter += 1
            elif dec_temp <= 1:
                controller = True

    while counter >= 0:
        if dec % 2 == 1:
            bits.append(1)
            counter -= 1
            dec = math.floor(dec/2)
        else:
            bits.append(0)
            counter -= 1
            dec = math.floor(dec/2)
    bits.reverse()
    print("\n")
    print(*bits, sep="")
    print("-----------------------------------------")
    print("\n")

def ToHex(int):
    hex_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    hex_out = []
    dec = int
    counter = len(str(dec)) - 1
    while counter >= 0:
        hex_out.append(hex_numbers[(dec % 16)])
        counter -= 1
        dec = math.floor(dec/16)
    hex_out.reverse()
    print("\n")
    print("0x",*hex_out, sep='')
    print("-----------------------------------------")
    print("\n")

print("Convert decimal number to binary or hex")

controller = True

while controller == True:
    print("Enter 'hex' to convert to hexidecimal and 'bit' to convert to binary")
    print("Type 'q' to quit")
    choice = input()

    if choice.lower() == 'hex':
        dec = int(input("Please enter an integer to convert: "))
        ToHex(dec)
    elif choice.lower() == 'bit':
        dec = int(input("Please enter an integer to convert: "))
        ToBinary(dec)
    elif choice.lower() == 'q':
        controller = False
    