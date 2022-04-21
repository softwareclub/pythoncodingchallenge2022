# Coding Challenge 2
# Name: Nishant Khadka
# Student No: 1017


'''
A Python Program to encode or decode set of characters provided by the user.

This program allows the user to choose between the encode mode and decode mode provided.
The program is also capable of encoding/decoding lines by reading/writing from a file
so that multiple messages can be encoded/decoded in one go.

'''

import os

# A tuple containing the set for default morse codes along with its value in English.
MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"),
    ("..-.", "F"), ("--.", "G"),("....", "H"), ("..", "I"), (".---", "J"),
    ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"), ("---", "O"),
    (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"),
    ("..-", "U"), ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"),
    ("--..", "Z"), (".-.-.-", "."), ("-----", "0"), (".----", "1"), ("..---", "2"),
    ("...--", "3"), ("....-", "4"), (".....", "5"), ("-....", "6"), ("--...", "7"),
    ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"), (".-...", "&"),
    ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"),
    ("-.-.--", "!")
)


def print_intro():
    '''Function to print the welcome messages to the user'''

    print()
    # Get terminal width to print the welcome message on centre of of the terminal
    print("Welcome to Wolmore".center(os.get_terminal_size().columns))
    print("This program encodes and decodes Morse code.".center(os.get_terminal_size().columns))
    for _ in range(os.get_terminal_size().columns):
        print('-', end='')
    print('\n')


def get_input():
    '''Function to request input from user to determine the mode of conversion,
        check to work on console or file and return three values
    '''

    # Loop until valid mode is entered by the user
    while True:
        mode = input("Would you like to encode (e) or decode (d) : ").lower()
        if (mode.lower()=='e' or mode.lower()=='d'):
            # Ask the user for file or console mode, after a valid operation mode is entered.
            file_choice = input("Would you like to read from a file (f) or the console (c)? ")
            if file_choice.lower()=='f':
                if mode.lower()=='e':
                    print("\nENCODING MODE USING FILE")
                else:
                    print("\nENCODING MODE USING FILE")
                # Loop until valid filename is entered.
                while True:
                    filename = input("Enter a filename: ")
                    if check_file_exists(filename):
                        # If valid filename is entered,
                        # exit the function after returning the three values.
                        return mode, None, filename
                    print('Invalid Filename')
            elif file_choice.lower()=='c':
                if mode.lower()=='e':
                    print("\nDECODING MODE USING CONSOLE")
                else:
                    print("\nDECODING MODE USING CONSOLE")
                if mode=='e':
                    message = input("What message would you like to encode: ")
                    return mode, message.upper(), None
                message = input("What message would you like to decode: ")
                return mode, message.upper(), None
        else:
            print("Invalid Mode")




def encode(message):
    '''Function to encode the provided message'''

    encoded_message = ''
    # Convert the message string into a list with each value separated by a space.
    message = message.split(' ')

    for word in message:
        for letter in word:
            for value in MORSE_CODE:
                # For each letter of the word in provided message,
                # check and append it's corresponding morse value from the MORSE_CODE tuple.
                if letter == value[1]:
                    encoded_message += value[0]
                    # Separate the characters by a space.
                    encoded_message += ' '
        # Separate the morse code for each word by three spaces.
        encoded_message += '   '
    return encoded_message



def decode(message):
    '''Function to decode the provided message'''

    decoded_message = ''
    # Convert the message string intro list,
    # separating the individual words provided by three spaces.
    message = message.split('   ')

    for word in message:
        characters = word.split(' ')
        for codes in characters:
            for values in MORSE_CODE:
                # For each value of the morse in provided message,
                # check and append it's corresponding character from the MORSE_CODE tuple.
                if codes == values[0]:
                    decoded_message += values[1]
        # Separate the words by a space.
        decoded_message += ' '

    return decoded_message



# ------------------------------ Challenge Functions ------------------------------



def process_lines(filename, mode):
    '''Function that takes filename and mode as parameters
        and reads the lines of file line by line and returns the encoded/decoded list
    '''

    result = []
    with open(filename, 'r', encoding="utf-8") as file:
        file_content = file.read()
    file_list = file_content.split('/')

    if mode == 'e':
        # Extract each line from the file for encoding.
        for words in file_list:
            # Encode each line from the file and append the result as a list item.
            # Remove the extra space that is created on the end of each list item.
            result.append(encode(words[:-1]))
    elif mode == 'd':
        # Extract each line from the file for decoding.
        for codes in file_list:
            result.append(decode(codes[:-1]))

    return result



def write_lines(lines):
    '''Function to write intro the file 'results.txt'''

    with open('results.txt', 'w', encoding="utf-8") as file:
        for values in lines:
            # Extract each value of the list and write it into the tile 'results.txt'.
            file.write(values)



def check_file_exists(filename):
    '''Function to check if given file exists'''

    try:
        # Return True if file is successfully opened.
        with open(filename, 'r', encoding="utf-8") as file_check:
            file_check.close()
        return True
    except FileNotFoundError:
        # Return False if any error is occured while trying to open file.
        return False



def main():
    '''MAIN DRIVER FUNCTION'''

    print_intro()
    input_values = get_input()

    if(input_values[0]=='e' and input_values[1] is None):
        # Call process_lines() if get_input() returns mode 'e' on file.
        write_lines(process_lines(input_values[2], input_values[0]))
        print('Output written to results.txt')
    elif(input_values[0]=='e' and input_values[2] is None):
        # Call encode() if get_input() returns mode 'e' on console.
        print('Encoded Message: ')
        print(encode(input_values[1]))
    elif(input_values[0]=='d' and input_values[1] is None):
        # Call process_lines() if get_input() returns mode 'd' on file.
        write_lines(process_lines(input_values[2], input_values[0]))
        print('Output written to results.txt')
    else:
        # Call decode() if get_input() returns mode 'e' on console.
        print('Decoded Message: ')
        print(decode(input_values[1]))


    # Loop until valid inputs are entered.
    while True:
        another = input("\nWould you like to encode/decode another message? (y/n): ").lower()
        if another=='y':
            input_values = get_input()
            if(input_values[0]=='e' and input_values[1] is None):
                write_lines(process_lines(input_values[2], input_values[0]))
                print('Output written to results.txt\n')
            elif(input_values[0]=='e' and input_values[2] is None):
                print('Encoded Message: ')
                print(encode(input_values[1]+'\n'))
            elif(input_values[0]=='d' and input_values[1] is None):
                write_lines(process_lines(input_values[2], input_values[0]))
                print('Output written to results.txt\n')
            else:
                print('Decoded Message: ')
                print(decode(input_values[1]))
        # Break the loop if user inputs 'n'.
        elif another == 'n':
            break

    print()
    # Print the goodbye message before terminating the program.
    for _ in range(os.get_terminal_size().columns):
        print('-', end='')
    print("Thanks for using the program, goodbye!".center(os.get_terminal_size().columns))



# Program execution begins here.
if __name__ == '__main__':
    main()
