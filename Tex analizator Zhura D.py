"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Dmytro Zhura
email: zhura.dm@seznam.cz
discord: twitch_dariys68
"""

# Registrovaní uživatelé
USERS = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Texty k analýze
TEXTS = [
    """Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an 
    elevation of more than 7500 feet above sea level. The butte is located just north of 
    US 30N and the Union Pacific Railroad, which traverse the valley.""",
    
    """At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the 
    Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from 
    the valley floor and steepen abruptly. Overlying them and extending to the top of the butte 
    are the much steeper buff-to-white beds of the Green River Formation, which are about 300 
    feet thick.""",
    
    """The monument contains 8198 acres and protects a portion of the largest deposit of 
    freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple 
    limestone layers, which lie some 100 feet below the top of the butte. The fossils represent 
    several varieties of perch, as well as other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."""
]

def authenticate_user():
    """
    Funkce pro ověření uživatele.
    """
    username = input("username: ")
    password = input("password: ")
    if username in USERS and USERS[username] == password:
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
        return True
    else:
        print("unregistered user, terminating the program..")
        return False

def analyze_text(text):
    """
    Funkce pro analyzu textu.
    """
    word_count = len(text.split())
    titlecase_count = sum(1 for word in text.split() if word.istitle())
    uppercase_count = sum(1 for word in text.split() if word.isupper())
    lowercase_count = sum(1 for word in text.split() if word.islower())
    numbers = [int(word) for word in text.split() if word.isdigit()]
    sum_numbers = sum(numbers)

    word_lengths = [len(word.strip('.,?!')) for word in text.split()]
    word_length_counts = {length: word_lengths.count(length) for length in set(word_lengths)}
    
    print("----------------------------------------")
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {len(numbers)} numeric strings.")
    print(f"The sum of all the numbers {sum_numbers}")

    print("----------------------------------------")
    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    for length, count in sorted(word_length_counts.items()):
        print(f"{str(length).ljust(2)} | {'*' * count} | {count}")

def main():
    """
    Hlavni funkce programu.
    """
    if authenticate_user():
        print("We have 3 texts to be analyzed.")
        while True:
            try:
                selection = int(input("Enter a number btw. 1 and 3 to select: "))
                if selection < 1 or selection > 3:
                    print("Invalid input. Please enter a number between 1 and 3.")
                    continue
                else:
                    analyze_text(TEXTS[selection - 1])
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()