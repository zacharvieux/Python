'''INF360 - Programming in Python

Assignment 3

I,     Zach Arvieux   , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

'''

#Step 1
#(5/5 points) Create a dictionary for each vehicle that contains the fields/keys and values listed above.

a = {"Name":"Ka", "Year Introduced": 1996, "Production of the Current Model": 2014, "Generation": "3rd", "Vehicle Information": "Developed by Ford Brazil as a super mini car"}
b = {"Name":"Fiesta", "Year Introduced": 1976, "Production of the Current Model": 2017, "Generation": "7th", "Vehicle Information": "Ford's long running subcompact line based on global B-car Platform"}
c = {"Name":"Focus", "Year Introduced": 1998, "Production of the Current Model": 2018, "Generation": "3rd", "Vehicle Information": "Ford's Compact car based on global C-car platform"}
d = {"Name":"Mondeo", "Year Introduced": 1992, "Production of the Current Model": 2012, "Generation": "2nd", "Vehicle Information": "Mid sized passenger sedan with 'One-Ford' design based on CD4 platform"}
e = {"Name":"Fusion", "Year Introduced": 2005, "Production of the Current Model": 2014, "Generation": "5th", "Vehicle Information": "Similar to Mondero"}
f = {"Name":"Taurus", "Year Introduced": 1986, "Production of the Current Model": 2009, "Generation": "6th", "Vehicle Information": "Full sized car based on D3 platform"}
g = {"Name":"Fiesta ST", "Year Introduced": 2013, "Production of the Current Model": 2013, "Generation": "1st", "Vehicle Information": "Fiesta's high performance factory tune"}
h = {"Name":"Focus RS", "Year Introduced": 2015, "Production of the Current Model": 2015, "Generation": "1st", "Vehicle Information": "Special high performance Focus developed by SVT"}
i = {"Name":"Mustang", "Year Introduced": 1964, "Production of the Current Model": 2014, "Generation": "6th", "Vehicle Information": "Ford's long running pony/muscle car"}
j = {"Name":"GT", "Year Introduced": 2004, "Production of the Current Model": 2016, "Generation": "2nd", "Vehicle Information": "Ford's limited production super car inspired by the legendary race car GT40"}

#Step 2
#(5/5 points) Write a function that will take a list of these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.

ford = [a,b,c,d,e,f,g,h,i,j]

def create_auto_dict(ford):
    auto_dict = {}
    for auto in ford:
        name = auto["Name"]
        auto_dict[name] = auto
    return auto_dict

#Step 3
#(5/5 points) Write a function that will go through the newly created dictionary and return a list of all the car's names, sorted alphabetically.

def get_sorted_name(auto_dict):
    names = []
    for key in auto_dict.keys():
        names.append(key)
    names.sort()
    return names

#Step 4    
#(5/5 points) Write a function that will go through the newly created dictionary return a dictionary of all the cars names and year introduced.

def car_year(auto_dict):
    years = {}
    for auto in auto_dict.values():
        year = auto["Year Introduced"]
        name = auto["Name"]
        years[year] = name
    return years

#Step 5
#(5/5 points) Use a print statement to show the results of the function from step 3, each on their own line.

auto_dict = create_auto_dict(ford)

print("Sorted by Name:")
sorted_names = sorted(auto_dict)
for name in sorted_names:
    print(name)

#Step 6
#(5/5 points) Use a print statement to show the results of the function from step 4 to display in the format: year : name. Sort by year introduced.

print()

print("Sorted by year:")
years_dict = car_year(auto_dict)
for year in sorted(years_dict.keys()):
    print(f"{year} : {years_dict[year]}")
    
