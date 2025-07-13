# Step 1: Setting Constants for Default Character, Vowel String.
# Vowel as List and Vowels as Dictionary

DEFAUTL_CHAR ='A'
VOWEL = 'AEIOU'

# Creating vowels Object from sequence of Vowel Characters
VOWELS = list(VOWEL)

#  Creating a vowels DICT and setting all the keys vowel characters and value as vowel
VOWEL_DICT = dict.fromkeys(VOWELS,"Vowel")

print(f"VOWEL List Type: {type(VOWELS)}",
      f"VOWEL DICT Type: {type(VOWEL_DICT)}", sep='\n')

print(f"Vowel List: {VOWELS}", f"VOWEL Dict: {VOWEL_DICT}", sep='\n')

# Step2: Take user input
user_input = input("Enter a single character (A-Z): ")

char = len(user_input) == 0 and DEFAUTL_CHAR or user_input[0].upper()

char = char.isalpha() and char or DEFAUTL_CHAR

print(f"The character {char} is a ",
      f"{char in VOWELS and 'Vowel' or 'Consonant'}")

print(f"The character {char} is a ",
      f"{VOWEL_DICT.get(char, 'Consonent')}")