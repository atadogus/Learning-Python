# Caesar cipher

def encrypt(input, shift):
    characters = list(input)
    characters_indices = []
    for char in characters:
        characters_indices.append(ord(char) + shift) # ord method converts a character into an into an integer value
    characters = []
    for index in characters_indices:
        characters.append(chr(index)) # chr method converts an integer value into a character
    encrypted_message = "".join(characters)
    return encrypted_message

def decrypt(input, shift):
    characters = list(input)
    characters_indices = []
    for char in characters:
        characters_indices.append(ord(char) - shift) # ord method converts a character into an into an integer value
    characters = []
    for index in characters_indices:
        characters.append(chr(index)) # chr method converts an integer value into a character
    decrypted_message = "".join(characters)
    return decrypted_message

# the two above are return type functions which return a variable type when called

message = str(input("Enter the message you want to encrypt: "))
key = int(input("Enter an integer value to determine how much you want to shift the characters of your message: "))

new_message = encrypt(message, key)
print(new_message)
old_message = decrypt(new_message, key)
print(old_message)

