"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Anastasija Kozlovska
email: kozlovska.st@gmail.com
discord: anastasia0163

"""
import task_template

# Vyžádát od uživatele přihlašovací jméno a heslo

name = input("Napiš svoje přihlašovací jméno:")
password = input("Napiš heslo:")

# zjistit zga uzivatel registrovany

registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

if name in registered_users and password == registered_users[name]:
    print("--" * 25)
    print(f"Welcome to the app {name}\nWe have 3 texts to be analyzed")
    print("--" * 25)
else:
    print("Unregistered user, terminating the program..")
    quit()
       

while True:

    user_choice = input("Enter a number btw. 1 and 3 to select:")

    if user_choice.isdigit() and 1 <= int(user_choice) <= len(task_template.TEXTS):
        user_text = task_template.TEXTS[int(user_choice) - 1]
        break
    else:
        print("The entered text number does not exist. Please try again.")

how_many_words = 0
capitalized_words = 0
small_letters = 0
big_letters = 0
numbers = 0
sum_numbers = 0

for words in user_text.split():
    how_many_words += 1

    if words.istitle():
        capitalized_words += 1
    elif words.islower():
        small_letters += 1
    elif words.isupper():
        big_letters += 1
    elif words.isdigit():
        numbers += 1
        sum_numbers += int(words)

print("--" * 25)
print(f"There are {how_many_words} words in the selected text.")
print(f"There are {capitalized_words} titilecase words.")
print(f"There are {small_letters} lowercase words.")
print(f"There are {big_letters} uppercase words.")
print(f"There are {numbers} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}")
print("--" * 25)
print("LEN|  OCCURANCES   |NR.")
print("--" * 25)
        
word_length = []
for word in user_text.split():
    pure_word = word.strip(".,:;")
    word_length.append(len(pure_word))

occurrence_words = {}
for value in range(1, max(word_length) + 1):
    occurrence_words[value] = word_length.count(value)    
for long, occurrence in occurrence_words.items():
        stars = "*" * occurrence
        print(f"{long:3}|   {stars:12}|{occurrence}")


    
