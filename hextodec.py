# Title: Program converting hex to binary
# Author: Conor
# Date: 07/11

def hex_to_binary(hex_string):
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    hex_string = hex_string.upper()
    binary_string = ""
    
    for char in hex_string:
        if char in hex_to_bin_map:
            binary_string += hex_to_bin_map[char]
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    
    return binary_string

# Example 
if __name__ == "__main__":
    hex_input = input("Enter a hexadecimal number: ")
    try:
        binary_output = hex_to_binary(hex_input)
        print(f"Binary representation: {binary_output}")
    except ValueError as e:
        print(e)
