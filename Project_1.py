"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Anastasija Kozlovska
email: kozlovska.st@gmail.com
discord: anastasia0163

"""
# Vyžádát od uživatele přihlašovací jméno a heslo

jmeno = input("Napiš svoje přihlašovací jméno:")
heslo = input("Napiš heslo:")

# zjistit zga uzivatel registrovany

registrovane_uzivatele = {"bob": 123, "ann": "pass123", "mike": "password123", "liz": "pass123"}

if jmeno in registrovane_uzivatele:
    print("--" * 25)
    print(f"Welcome to the app {jmeno}\nWe have 3 texts to be analyzed")
    print("--" * 25)
else:
    print("Unregistered user, terminating the program..")
      
 
TEXTS = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]


vyber = input("Enter a number btw. 1 and 3 to select:")

if vyber.isdigit() and 1 <= int(vyber) <= 3:
    vybrany_text = TEXTS[int(vyber) - 1]
    pocet_slov = 0
    pismena_s_velkym = 0
    mala_pismena = 0
    velka_pismena = 0
    pocet_cisel = 0
    sum_cisel = 0
    for slova in vybrany_text.split():
        pocet_slov += 1
        if slova.istitle():
            pismena_s_velkym += 1
        elif slova.islower:
            mala_pismena += 1
        elif slova.isupper:
            velka_pismena += 1
        elif slova.isdigit():
            pocet_cisel += 1
            sum_cisel += int(slova)
    print("--" * 25)
    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {pismena_s_velkym} titilecase words.")
    print(f"There are {mala_pismena} lowercase words.")
    print(f"There are {velka_pismena} uppercase words.")
    print(f"There are {pocet_cisel} numeric strings.")
    print(f"The sum of all the numbers {sum_cisel}")
    print("--" * 25)
    print("LEN|  OCCURANCES  |NR.")
    print("--" * 25)
        
    delka_slova = []
    for slovo in slova:
        delka_slova.append(len(slovo))

    vyskyt_slov = {}
    for value in range(1, max(delka_slova) + 1):
        vyskyt_slov[value] = delka_slova.count(value)    
    for delka, vyskyt in vyskyt_slov.items():
            hvezdicky = "*" * vyskyt
    print(f"{delka:3}|{hvezdicky:14}|{vyskyt}")
else:
    print("The entered text number does not exist. Please try again.")

    
