"""
Xavier Pitsilos
05/04/2022 - 05/04/2022
Generates a secure password with a mix of letters, numbers and symbols
"""
import string
import random

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
numbers = (tuple([str(i) for i in range(11)]))
symbols = (':', "'", '~', '+', '[', '\\', '^', '{', '%', '(', '-', '@', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/')

def generatePassword(pass_length: int = 10, char_type_split: list = [3, 3, 2, 2]):
    """
    :param pass_length: The length that the password will be
    :param char_type: The split of different that the password will contain in
                      the order lowercase letters, uppercase letters, numbers,
                      symbols
                      example- char_type_split=[3, 3, 2, 2] will include 3
                      uppercase letters, 3 lowercase letters, 2 numbers and
                      2 symbols
    """
    if sum(char_type_split) != pass_length:
           raise Exception('pass_length must be equal to the total sum of char_type_split')

    password = ''
    password = random.choices(lowercase_letters, k=char_type_split[0]) + random.choices(uppercase_letters, k=char_type_split[1]) + random.choices(numbers, k=char_type_split[2]) + random.choices(symbols, k=char_type_split[3]) # k = amount of items to return 
    password = random.sample(password, len(password)) # shuffles the items by selecting random characters in our password that can not be reused (equal to the amount of times of our password length)
    password = ''.join(password)
    print(password)
    
generatePassword()
