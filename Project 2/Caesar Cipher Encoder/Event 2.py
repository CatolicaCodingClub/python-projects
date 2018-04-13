# Caesar Cipher (retrieved from https://inventwithpython.com/chapter14.html)

MAX_KEY_SIZE = 26 #MAX_KEY_SIZE is a constant that stores the integer 26 in it. MAX_KEY_SIZE reminds us that in this program, the key used in the cipher should be between 1 and 26.

def getMode(): #The getMode() function will let the user type in if they want encryption or decryption mode for the program. 

    while True: #The while statement takes an expression and executes the loop body while the expression evaluates to (boolean) "true". 

        print('Do you wish to encrypt or decrypt a message?')

        mode = input().lower() # The value returned from input() and lower() is stored in mode.The method lower() returns a copy of the string in which all case-based characters have been lowercased.

        if mode in 'encrypt e decrypt b'.split(): #The if statement’s condition checks if the string stored in mode exists in the list returned by 'encrypt e decrypt d'.split().
        # Therefore, getMode() will return the string 'e' or the string 'd'. Split() splits or breakups a string and adds the data to a string array using a defined separator.
            return mode

        else:

            print('Enter either "encrypt" or "e" or "decrypt" or "b".') #In the case the answer is not "encrypt" or "decrypt".

def getMessage():

    print('Enter your message:')

    return input()

def getKey(): #The getKey() function lets the player type in the key they will use to encrypt or decrypt the message.

    key = 0

    while True: #The while loop ensures that the function keeps looping until the user enters a valid key.

        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) # % Modulus: Divides left hand operand by right hand operand and returns remainder (ex. b % a = 0).
        # %s	string conversion via str() prior to formatting. This operator is unique to strings.
        key = int(input()) #The int() method returns an integer object from any number or string.

        if (key >= 1 and key <= MAX_KEY_SIZE):

            return key
       
def getTranslatedMessage(mode, message, key): #getTranslatedMessage() does the encrypting and decrypting. It has three parameters: mode sets the function to encryption mode or decryption mode; message is the plaintext (or ciphertext) to be encrypted (or decrypted).; key is the key that is used in this cipher.

    if mode[0] == 'b': #Checks if the first letter in the mode variable is the string 'd'. If so, then the program is in decryption mode. The only difference between the decryption and encryption mode is that in decryption mode the key is set to the negative version of itself.
        # == means equal
        key = int(-key) #Encryp = -Decrypt

    translated = '' #translated is the string of the result: either the ciphertext (if you are encrypting) or the plaintext (if you are decrypting). It starts as the blank string and has encrypted or decrypted characters concatenated to the end of it.

    for symbol in message: #for loop iterates over each letter (in cryptography they are called symbols) in the message string. On each iteration through this loop, symbol will have the value of a letter in message.

        if symbol.isalpha(): # Only letters will be encrypted or decrypted. Numbers, punctuation marks, and everything else will stay in their original form. 

            num = ord(symbol) # The num variable will hold the integer ordinal value of the letter stored in symbol. 

            num += key # “Shifts” the value in num by the value in key.
            # += adds a number to a variable, changing the variable itself in the process (whereas + would not). 
       
        #DOUBTS IN THE NEXT TWO IFS!
        
        if symbol.isupper(): # Checks if the symbol is an uppercase letter.

            if num > ord('Z'): # Check if num has a value larger than the ordinal value for “Z”. If so, then subtract 26 (because there are 26 letters in total) from num. After doing this, the value of num is 68. 68 is the correct ordinal value for 'D'.
                
                num -= 26
                # subtracts a value from variable, setting the variable to the result
            elif num < ord('A'):
            #The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE. Unlike else, for which there can be at most one statement, there can be an arbitrary number of elif statements following an if.
                num += 26

        elif symbol.islower(): 

                if num > ord('z'):

                    num -= 26

                elif num < ord('a'):

                    num += 26

        translated += chr(num) # Concatenates the encrypted/decrypted character to the translated string.
        # The chrt() method returns a character (a string) from an integer (represents unicode code point of the character).
    else:
                
        translated += symbol #If the symbol was not an uppercase or lowercase letter, then it concatenates the original symbol to the translated string. Therefore, spaces, numbers, punctuation marks, and other characters won’t be encrypted or decrypted.

    return translated

mode = getMode()

message = getMessage()

key = getKey()

print('Your translated text is:')

print(getTranslatedMessage(mode, message, key))