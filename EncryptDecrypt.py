import random
import string

def generate_cipher_key():
    ''' this function will generate a cipher for user_input text'''
    # Generate a random permutation of the alphabet, digits, and special characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # print(all_characters) this is string => a-z, A-Z, 0-9, and all special characters
    cipher_key = list(all_characters)
    
    # randomly shuffle the values 
    random.shuffle(cipher_key)
    # print(cipher_key) this is list format of all_characters 
    
    # zip() -> tuple   => but here, we are making, all_characters->key and  cipher_key-> values
    return dict(zip(all_characters, cipher_key)) 

# encrypt the user input - text
def encrypt(text, cipher_key):
    encrypted_text = ""
    for char in text:
        # use get() -> to avoid errors of key,values 
        # += because consider the previous encrypt key also as it is a string 
        encrypted_text += cipher_key.get(char, char)
    return encrypted_text

# decrypt back 
def decrypt(encrypted_text, cipher_key):
    # reverse the key,value form original cipher_key  ->  keys->values , values->keys now
    reversed_cipher_key = {v: k for k, v in cipher_key.items()}
    decrypted_text = ""
    for char in encrypted_text:
        # += because consider the previous decrypt key also as it is a string 
        decrypted_text += reversed_cipher_key.get(char, char)
    return decrypted_text