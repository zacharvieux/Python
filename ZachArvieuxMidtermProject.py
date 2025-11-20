'''

INF360 - Programming in Python

Assignment Midterm Project

I, Zach Arvieux , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Star Wars Name Generator

This will make random Star Wars-style Names with titles and extras.
It will ask the user how many they want and prints a list.
There are over 58 million possible combinations.

'''

import random

#============
# Name Parts
#============

first_name_1 = ["an", "qui", "obi", "lu", "re", "ky", "ma", "pa", "fi", "sha", "ka", "zi", "jor", "tho", "dra", "vek", "sar", "ben", "tor", "nal"]
first_name_2 = ["a", "lo", "mi", "ni", "ra", "ta", "do", "en", "ri", "zo", "va", "el", "is", "or", "in", "un", "ex", "an", "ar", "ok"]
last_name_1 = ["sky", "ken", "org", "cal", "tan", "da", "ren", "jin", "vis", "kat", "zor", "vek", "dra", "mor", "val", "sen", "cor", "zan", "lux", "thr"]
last_name_2 = ["walker", "obi", "ana", "riss", " solo", "lor", "do", "dax", " vox", "renn", "vek", "thorn", "voss", "darr", "rix", "korr", "val", "mar", "zek", "nox"]
titles = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", " Darth", " Jedi", " Master", " Padawan", " Sith", " Lord"]
extras = ["", "", "", "", "", "", " of Tatooine", " of Corellia", " of Alderaan", " of Naboo", " of Coruscant", " of Endor", " of Kashyyyk", " of Jakku", " of Cloud City", " the Hutt"]


#===========
# Functions
#===========

#Get the number of names wanted and return an integer.
def get_name_count():
    while True:
        count_input = input ("How many names do you want? (example: 5): ")
        if count_input.isdigit():
            return int(count_input)
        else:
            print("Please use a valid number")
            print("-------------------------")

#Generate one randomized Star War-style full name.
def generate_name():
    title = random.choice(titles)
    first = random.choice(first_name_1) + random.choice(first_name_2)
    last = random.choice(last_name_1) + random.choice(last_name_2)
    extra = random.choice(extras)
    full_name = (title + " " + first + " " + last + extra).title()
    return full_name

#Print the list of names
def print_names(count):
    print("\nHere are your names:")
    print("-------------------------")
    for i in range(count):
        name = generate_name()
        print(f"{i+1}. {name}")

#Main Program loop
def main():
    print("Star Wars Name Generator")
    print("-------------------------")
    count = get_name_count()
    print_names(count)
    print("-------------------------")
    input("\nPress Enter to Exit...")

#=================
# Run the program
#=================
    
main()
