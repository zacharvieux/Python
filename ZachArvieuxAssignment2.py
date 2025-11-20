'''INF360 - Programming in Python

Assignment 2

I,     Zach Arvieux   , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

'''


import random

randomNumber = random.randint(1,10)

    
print("Hi!, what year were you born?")

print("Full year, Please!")

while True:
    yrbrn = input('>:')
    if int(yrbrn) >= 0:
        break
    else:
        print("That is not a valid year. Please put in the correct year")
        continue
    
for i in range(0,randomNumber):
    print("-" * i)
    
if int(yrbrn) == 2025:
    print("You must have just been born!")
elif int(yrbrn) < 1945 and int(yrbrn) >= 0:
    print("You are older than Dirt!")
elif int(yrbrn) <= 1964:
    print("You are part of the Boomer generation!")
elif int(yrbrn) <= 1980:
    print("You are part of Generation X!")
elif int(yrbrn) <= 1996:
    print("You are a Millennial!")
elif int(yrbrn) <= 2012:
    print("You are part of Generation Z!")
elif int(yrbrn) <= 2024:
    print("You are part of Generation Alpha!")
else:
    print("You couldn't have been born yet!")
