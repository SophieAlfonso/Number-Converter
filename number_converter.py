# This function converts a hex digit to its decimal equivalent
def hex_char_decode(digit):
    hex_assign = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}       # A dictionary of hex conversions

    num = int(digit) if digit.isdigit() else hex_assign[digit]

    return num      # Return the converted number

# This function converts a hex string to a decimal value
def hex_string_decode(hex):
    dec = 0
    power = len(hex) - 1

    for i in hex:                   # Convert each element of the hex string
        multi = hex_char_decode(i)  # Call the digit converter
        d = multi * (16 ** power)   # Multiply by 16 to the respective power
        dec += d

        power -= 1

    return dec      # Return the converted string

# This function converts a binary string to decimal
def binary_string_decode(binary):
    power = len(binary) - 1
    dec = 0

    for digit in binary:        # Convert each element in the string
        if digit == '0':

            d = 0
        elif digit == '1':      # If it's a 1, multiply by 2 to the respective power
            d = 2 ** power

        dec += d
        power -=1

    return dec      # Return the converted string

# This function converts a binary string to hex
def binary_to_hex(binary):
    count = 0       # Define a counting variable
    quad = ''       # Make a temporary string to evaluate each group of four
    hex_str = ''    # Make a string to keep track of your converted hex values
    hex_assign = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}     # A dictionary for hex conversions

    # Find the amount of the binary string not grouped in fours
    rem = len(binary) % 4

    if rem != 0:        # If there exists a group of not four, find the hex conversion
        length = rem
        power = length - 1
        d = 0

        for d2 in binary[0:length]:     # Convert the binary string not grouped in four
            if d2 == '1':
                d += 2 ** power
            power -= 1

        num = str(d) if d < 10 else hex_assign[d]
        hex_str += num

    while count < (len(binary) - rem):      # Convert the rest of the binary string
        for digit in binary[rem:]:
            count += 1
            quad += digit       # Add each digit in a group of four to the quad string


            if count % 4 == 0:  # For each group of four, convert
                power = 3
                d = 0

                for digit2 in quad:
                    if digit2 == '1':
                        d += 2 ** power
                    power -= 1

                num = str(d) if d < 10 else hex_assign[d]

                hex_str += num  # Add each variable to the hex string
                quad = ''       # Reset the quad string

    return hex_str  # Return the hex string

# Define the main function
def main():
    c = 1       # Define the choice variable

    while c != 4:       # Create a loop for as long as the choice is not to quit
        print('Decoding Menu\n'         # Display the menu
              '-------------\n'
              '1. Decode hexadecimal\n'
              '2. Decode binary\n'
              '3. Convert binary to hexadecimal\n'
              '4. Quit\n')

        c = int(input('Please enter an option: '))      # Get the choice

        if c == 4:      # If the choice is 4, quit
            print('Goodbye!')
            break

        str0 = input('Please enter the numeric string to convert: ')    # Get the string to convert

        str1 = str0.lower()
        id = str0[0:2]      # Identify if the string starts with '0b' or '0x'

        if id == '0x':      # If it does, remove it
            str2 = str1.replace('0x', '')
        elif id  == '0b':
            str2 = str1.replace('0b', '')
        else:
            str2 = str1


        if c == 1:      # If the choice is 1, call the hex_string_convert function
            result = hex_string_decode(str2)

        if c == 2:      # If the choice is 2, call the binary_string_convert function
            result = binary_string_decode(str2)

        if c == 3:      # If the choice is 3, call the binary_to_hex function
            result = binary_to_hex(str2)

        print(f'Result: {result}')      # Print the result
        print()

if __name__ == '__main__':
    main()
