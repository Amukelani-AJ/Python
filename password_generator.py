import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #Build a string containing all possible values
    characters = letters
    #Validating selected parameters : if num Tru add it to string , if special_char true add it to string
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False  #Variable for checking if the word meets the selected param
    has_number = False
    has_special = False

    #Check while meets_criteria is not true and password length is less than the given length keep looping
    while not meets_criteria or len(password) < min_length:
         new_char = random.choice(characters) # Pick a random value from the character string containing all possible chars
         password += new_char #Add the random char into the password

