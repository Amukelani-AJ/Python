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

    while not meets_criteria or len(password) < min_length:
         pass
