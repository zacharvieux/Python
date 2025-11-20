'''
INF360 - Programming in Python
Assignment 4
I,Zach Arvieux , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

import re

#  Read the file story.txt and store the lines as a variable called story

storyfile = open("story.txt")
story = storyfile.readlines()
storyfile.close()

# Regular expression that will find all occurances of the phrase, "Sherlock Holmes"

sherlock = re.compile(r'Sherlock Holmes')

foundCount = 0
new_story_lines=[]

for line in story:

# Storing the count of these occurances as a variable called foundCount

    matching = sherlock.findall(line)
    foundCount += len(matching)

#  Using the substitue method, replace all occurances of "Sherlock Holmes" with your name

    new_line = sherlock.sub("Zach Arvieux", line)
    new_story_lines.append(new_line)

# Write a regular expression that will find all occurances of the phrase, "the"

the = re.compile(r"\bthe\b", re.IGNORECASE)

# A variable called theCount, that stores the total number of occurances of the phrase "the".

theCount = 0

for line in story:
    the_matches = the.findall(line)
    theCount += len(the_matches)

#Save the story out to a new file called new_story.txt.

new_file = open("new_story.txt", "w")
new_file.writelines(new_story_lines)
new_file.close()

#Print to the user, the original name, the replacement name, and the total number of occurances using a print command with a formatted string literal using a string that starts with f"

print(f'Original name: "Sherlock Holmes" -> Replacement name: "Zach Arvieux" Total replacements made (foundCount): {foundCount}')

#Print to the user the a string that tells the user the total number of occurances of "the" using a print command with a formatted string literal using a string that starts with f".

print(f'Total occurrences of the word "the" (theCount):{theCount}')


