"""
INF360 - Programming in Python

Assignment Final Project

I, Zach Arvieux , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.


Description:
    This program generates random Star Wars-style character names using
    combinations of name fragments, titles, and extra descriptors. It allows
    the user to:

        - Generate a chosen number of new names
        - View the history of names generated in this session
        - Save the generated names to a text file
        - View short lore descriptions for different Star Wars-style factions

"""

import random
import logging
from pathlib import Path

# ==========================
# Logging Configuration
# ==========================

# Configure the logging module. Logs will be written to starwars_name_generator.log.
logging.basicConfig(
    filename="starwars_name_generator.log",
    level=logging.DEBUG,  # Capture debug and above
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==========================
# Object-Oriented Core
# ==========================


class StarWarsNameGenerator:
    """
    A class responsible for generating Star Wars-style character names and
    storing a history of generated names.
    """

    def __init__(self):
        
        self.first_name_1 = [
            "an", "qui", "obi", "lu", "re", "ky", "ma", "pa", "fi", "sha",
            "ka", "zi", "jor", "tho", "dra", "vek", "sar", "ben", "tor", "nal"
        ]
        self.first_name_2 = [
            "a", "lo", "mi", "ni", "ra", "ta", "do", "en", "ri", "zo",
            "va", "el", "is", "or", "in", "un", "ex", "an", "ar", "ok"
        ]
        self.last_name_1 = [
            "sky", "ken", "org", "cal", "tan", "da", "ren", "jin", "vis", "kat",
            "zor", "vek", "dra", "mor", "val", "sen", "cor", "zan", "lux", "thr"
        ]
        self.last_name_2 = [
            "walker", "obi", "ana", "riss", " solo", "lor", "do", "dax", " vox",
            "renn", "vek", "thorn", "voss", "darr", "rix", "korr", "val", "mar",
            "zek", "nox"
        ]
        self.titles = [
            "", "", "", "", "", "", "", "", "", "", "", "", "", " Imperial", " Rebel", " Smuggler",
            " Bounty Hunter", " Darth", " Jedi", " Master", " Padawan", " Sith", " Lord"
        ]
        self.extras = [
            "", "", "", "", "", "",
            " of Tatooine", " of Corellia", " of Alderaan", " of Naboo",
            " of Coruscant", " of Endor", " of Kashyyyk", " of Jakku",
            " of Cloud City", " the Hutt"
        ]

        self.factions = {
            "Jedi": "Guardians of peace and justice in the galaxy.",
            "Sith": "Dark side users who seek power and domination.",
            "Bounty Hunter": "Mercenaries who hunt targets for credits.",
            "Smuggler": "Shady operators who move cargo through blockades.",
            "Rebel": "Fighters against oppressive regimes.",
            "Imperial": "Agents and soldiers of the Galactic Empire."
        }

        self.history = []

        logging.debug("StarWarsNameGenerator initialized.")

    def generate_name(self):
        """
        Generate a single random Star Wars-style name using the configured
        fragments, and store it in the history list.
        """
        try:
            title = random.choice(self.titles)
            first = random.choice(self.first_name_1) + random.choice(self.first_name_2)
            last = random.choice(self.last_name_1) + random.choice(self.last_name_2)
            extra = random.choice(self.extras)

            full_name = (title + " " + first + " " + last + extra).title()
            self.history.append(full_name)

            logging.debug("Generated name: %s", full_name)
            return full_name
        except Exception as e:
            logging.critical("Error generating name: %s", e)
            raise

    def generate_multiple(self, count):
        """
        Generate 'count' names and return them as a list.

        :param count: Number of names to generate (int)
        :return: List of generated names
        """
        names = []
        for _ in range(count):
            name = self.generate_name()
            names.append(name)
        logging.debug("Generated %d names.", count)
        return names

    def get_history(self):
        """
        Return the list of all names generated in this session.
        """
        return list(self.history)

    def get_factions(self):
        """
        Return a list of available faction names.
        """
        return list(self.factions.keys())

    def describe_faction(self, faction_name):
        """
        Return the lore description for a given faction.

        :param faction_name: Key in the factions dictionary
        :return: Description string, or a default message if not found
        """
        description = self.factions.get(faction_name, "Unknown faction.")
        logging.debug("Faction '%s' description requested.", faction_name)
        return description


# ==========================
# Helper Functions (Flow)
# ==========================

def get_menu_choice():
    """
    Display the main menu and return the user's choice as an int from 1 to 5.
    Uses input validation and logs invalid attempts.
    """
    print("\nStar Wars Name Generator")
    print("-------------------------")
    print("1. Generate new names")
    print("2. View name history")
    print("3. Save history to file")
    print("4. View faction descriptions")
    print("5. Exit")

    while True:
        choice = input("Choose an option (1-5): ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            logging.debug("User selected menu choice: %s", choice)
            return int(choice)
        else:
            print("Please enter a number between 1 and 5.")
            logging.warning("Invalid menu choice entered: %s", choice)


def get_name_count():
    """
    Ask the user how many names they want to generate and return a valid int.
    Repeats until a valid positive integer is provided.
    """
    while True:
        user_input = input("How many names do you want to generate? (example: 5): ").strip()
        if user_input.isdigit():
            count = int(user_input)
            if count > 0:
                logging.debug("User requested %d names.", count)
                return count
            else:
                print("Please enter a number greater than 0.")
                logging.warning("User entered non-positive count: %s", user_input)
        else:
            print("Please use a valid positive whole number.")
            logging.warning("User entered invalid count: %s", user_input)


def save_history_to_file(names, filename="starwars_names.txt"):
    """
    Save the given list of names to a text file, one name per line.
    """
    if not names:
        print("No names in history to save yet.")
        logging.info("User attempted to save empty history.")
        return

    path = Path(filename)

    try:
        with path.open("w", encoding="utf-8") as f:
            for name in names:
                f.write(name + "\n")

        print(f"Saved {len(names)} names to '{filename}'.")
        logging.info("Saved %d names to file: %s", len(names), filename)
    except Exception as e:
        print("An error occurred while saving the file.")
        logging.critical("Failed to save names to file '%s': %s", filename, e)


def display_history(names):
    """
    Print the history of generated names in a numbered list.
    """
    if not names:
        print("\nNo names have been generated yet.")
        logging.info("User requested history but history is empty.")
        return

    print("\nGenerated Name History")
    print("-------------------------")
    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")


def display_faction_descriptions(generator):
    """
    Show all factions and their descriptions using the generator's dictionary.
    """
    factions = generator.get_factions()
    if not factions:
        print("No faction information available.")
        logging.warning("No factions found in generator.")
        return

    print("\nFaction Descriptions")
    print("-------------------------")
    for faction in factions:
        description = generator.describe_faction(faction)
        print(f"{faction}: {description}")


# ==========================
# Main Program Loop
# ==========================

def main():
    """
    Main function that drives the menu-based interaction with the user.
    """
    logging.info("Program started.")
    generator = StarWarsNameGenerator()

    while True:
        choice = get_menu_choice()

        if choice == 1:
            # Generate new names
            count = get_name_count()
            names = generator.generate_multiple(count)

            print("\nHere are your names:")
            print("-------------------------")
            for index, name in enumerate(names, start=1):
                print(f"{index}. {name}")

        elif choice == 2:
            # View history
            history = generator.get_history()
            display_history(history)

        elif choice == 3:
            # Save history to file
            history = generator.get_history()
            save_history_to_file(history)

        elif choice == 4:
            # View faction descriptions
            display_faction_descriptions(generator)

        elif choice == 5:
            # Exit
            logging.info("User chose to exit the program.")
            print("Goodbye! May the Force be with you.")
            break

    logging.info("Program terminated.")


# Run the program only if this file is executed directly.
if __name__ == "__main__":
    main()
