def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !?.'

    values = keys[-1] + keys[0:-1]

    encrytDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))

    message = input("Enter your secret message: ")
    mode = input("Crypto Mode : Encode(E) OR Decode(D)")

    if mode.upper() == 'E':
        newMessage = ''.join([encrytDict[letter]
                              for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                              for letter in message.lower()])
    else:
        print("Please try again, wrong choice entered")

    return newMessage.capitalize()


print(machine())