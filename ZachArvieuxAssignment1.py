'''
INF360 - Programming in Python
Assignment 1
I,     Zach Arvieux , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''


print('Welcome to FHSU!')
print()
print('What is your Major')

myInput = input('>:')


print('You put in that your Major is ' + myInput)
print()
print('What year are you graduating?')
gradyear = input('>:')

print('How old are you now?')
myage = input('>:')

yearsleft = int(gradyear) - 2025

gradage = int(yearsleft) + int(myage)

print('You only have ' + str(yearsleft) + ' years till graduation!')
print()
print('You will be ' + str(gradage) + ' when you graduate!')

