MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-' }

# encryption
def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += " "
    return cipher

# decryption if the user has the morse code already
def decrypt(message):
    message += " "
    decipher = ""
    citext = ""

    for letter in message:
        if letter != " ":
            i = 0
            citext += letter
        else:
            i += 1

            if i == 2:
                decipher += " "
            else:
                for key, value in MORSE_CODE_DICT.items():
                    if citext == value:
                        decipher += key

                citext = ""
    return decipher

running = True
while running:
    userSelect = input("Would you like to Encrypt [1] message or Decrypt [2]? (Enter 1 or 2)\n")
    if userSelect == "1" or userSelect == "2":
        userMessage = input("Enter message: \n")
        if userSelect == "1":
            result = encrypt(userMessage.upper())
            result = "Encrypted message is: " + result
        elif userSelect == "2":
            result = decrypt(userMessage)
            result = "Decrypted message is: " + result
        print(userMessage)
        print(result)
        userContinue = input("Would you like to run again? [Select Y/N]\n")
        if userContinue != "Y":
            running = False
            if userContinue == "N":
                print("Thanks! Have a .-- --- -. -.. . .-. ..-. ..- .-.. day.")
            else:
                print("Selection not valid, will end program.")
    else:
        print("Selection not valid. Try again.")
