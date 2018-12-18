"""
create_COOP_prg.py

Creates a new program file for COOP. Gets chapter, exercise, and description from user.
Creates chapter directory, if it does not exist, at the same level as this program.

Algorithm
    Intro
    Program Loop: 1) Create/update profile; 2) Create program file; 3) Quit
    
    Create/update profile
        Check for existence of profile file (author, course, section, IDE)

    Create program file
        Get chapter, exercise, and description from user.
        Validate data (int chapter & exercise numbers < 100; no spaces in description)
        Force chapter and exercise numbers to be two digits
        Concatenate parts together in this format: U99_Ex99_description.py
        Check to see if chapter directory exists, creating if not
        Create program file in chapter directory
"""

import pathlib, sys, datetime

AUTHOR = 0
COURSE = 1
SECTION = 2
IDE = 3
SOURCE = 4
FILENAME = 5
EXERCISE = 6
CHAPTER = 7
INFO = ['', 'Coding for OOP', '', 'PyCharm', 'Python Programming', '', '', '']

if sys.platform[0:3] == 'win':
    SLASH = '\\'
else:
    SLASH = '/'                    # set to slash used by OS

PREFIX = ''          # used if new directory is not at current level; empty string otherwise
PROFILE_FILENAME = 'COOP_profile.txt'


def main():
    # Intro
    print("\nUse this program to create program files.")

    # Program Loop: 1) Create/update profile; 2) Create program file; 3) Quit
    while True:
        print("\nMAIN MENU")
        print("------------------------")
        print("1) Create/update profile")
        print("2) Create program file")
        print("0) Quit\n")
        choice = int(input("-> "))

        if choice == 0:
            break
        elif choice == 1:
            profile()
        elif choice == 2:
            program()
        else:
            print("\nPlease enter valid input.\n")


def profile():
    """
    Allows user to create/update the profile file

    Algorithm
        If profile file exists, read and print current contents
        Present menu allowing user to create (when file does not exist), update (when file does exist), or exit
        If create/update is chosen, get acknowledgement from user before writing
    """
    path = pathlib.Path(PROFILE_FILENAME)

    while True:
        pathExists = path.exists()
        print('\nCREATE/UPDATE PROFILE')
        print("-----------------------")

        if pathExists:
            print("1) Update")
        else:
            print("1) Create")

        print("2) Show current profile")
        print("0) Exit to Main Menu")
        choice = int(input("-> "))

        if choice == 0:
            break
        elif choice == 1:
            if pathExists:
                profile_update()
            else:
                profile_create()
        elif choice == 2:
            profile_show()
        else:
            print("\nPlease enter valid input.\n")


def profile_update():
    """
    Reads profile file and allows user to update info; writes changes to file
    """
    profile_read()
    profile_create()


def profile_create():
    """
    After calling edit routine, writes new profile info to profile file
    """
    profile_edit()
    csv_data = ''
    f = open(PROFILE_FILENAME, 'w')

    for item in INFO:
        csv_data += '{},'.format(item)

    print(csv_data[:-1], file=f, end='')
    f.close()


def profile_edit():
    """
    Editing "screen" used for both update() and create().

    Algorithm:
        Present each prompt with the current value as default
        If response is empty, use default, otherwise, replace with user input
    :param author: str -> author of program
    :param course: str -> computer course (defaults to 'Coding for OOP')
    :param section: str -> section number of class
    :param ide: str -> IDE used (defaults to 'PyCharm')
    :param source: str -> source of program assignment (defaults to 'Python Programming')
    :return: str * 5 -> edited strings
    """
    print("\nCREATING PROFILE")
    print("\nChange info by typing the replacement. Just hit Enter to accept the current value.\n")
    new_author  = input(' Author ({}): '.format(INFO[AUTHOR]))
    new_course  = input(' Course ({}): '.format(INFO[COURSE]))
    new_section = input('Section ({}): '.format(INFO[SECTION]))
    new_ide     = input('    IDE ({}): '.format(INFO[IDE]))
    new_source  = input(' Source ({}): '.format(INFO[SOURCE]))

    if new_author != "":
        INFO[AUTHOR] = new_author
    if new_course != "":
        INFO[COURSE] = new_course
    if new_section != "":
        INFO[SECTION] = new_section
    if new_ide != "":
        INFO[IDE] = new_ide
    if new_source != "":
        INFO[SOURCE] = new_source

    return


def profile_show():
    """
    Displays current profile
    """
    profile_read()
    print("\n\nCURRENT PROFILE")
    print(    "----------------------------")
    print(' Author: {}'.format(INFO[AUTHOR]))
    print(' Course: {}'.format(INFO[COURSE]))
    print('Section: {}'.format(INFO[SECTION]))
    print('    IDE: {}'.format(INFO[IDE]))
    print(' Source: {}'.format(INFO[SOURCE]))
    input("\nPress ENTER to continue...")


def profile_read():
    """
    Reads profile file and populates INFO list
    """
    global INFO
    f = open(PROFILE_FILENAME, 'r')
    INFO = f.readline().split(',')
    f.close()


def program():
    """
    Creates a program file using user-specified header info

    Algorithm
        Get chapter, exercise, and description from user.
        Validate data (int chapter & exercise numbers < 100; no spaces in description)
        Force chapter and exercise numbers to be two digits
        Concatenate parts together in this format: U99_Ex99_description.py
        Check to see if chapter directory exists, creating if not
        Create program file in chapter directory
    """
    profile_path = pathlib.Path(PROFILE_FILENAME)

    if not profile_path.exists():
        profile_create()

    INFO[CHAPTER], INFO[EXERCISE], description = get_header_info()
    chapter_dir = "Chapter{}".format(INFO[CHAPTER])
    INFO[FILENAME] = "U{}_Ex{}_{}.py".format(INFO[CHAPTER], INFO[EXERCISE], description)
    dir_path = pathlib.Path(PREFIX + chapter_dir)
    header = make_hdr()

    if not dir_path.exists() or not dir_path.is_dir():
        dir_path.mkdir()

    file_path = str(dir_path) + SLASH + INFO[FILENAME]

    f = open(file_path, 'w')
    print(header, file=f)
    f.close()


def make_hdr():
    return '''"""
{filename}

  Author: {author}
  Course: {course}
 Section: {section}
    Date: {date}
     IDE: {ide}
     
Assignment Info
  Exercise: {exercise}
    Source: {source}
   Chapter: {chapter}
   
Program Description


Algorithm


    
"""'''.format(filename=INFO[FILENAME], author=INFO[AUTHOR], course=INFO[COURSE],
              section=INFO[SECTION], date=datetime.date.today(), ide=INFO[IDE],
              exercise=INFO[EXERCISE], source=INFO[SOURCE], chapter=INFO[CHAPTER])


def get_header_info():
    print("\nPROGRAM HEADER INFO")
    print("-------------------")

    while True:
        ch = int(input("  Chapter: "))
        if not (ch > 0 and ch < 100):
            print("Chapter number must be positive and less than 100. Please correct.\n")
        else:
            break

    while True:
        ex = int(input(" Exercise: "))
        if not (ex > 0 and ex < 100):
            print("Exercise number must be positive and less than 100. Please correct.\n")
        else:
            break

    while True:
        desc = clean(input("Description: "))
        if desc == "":
            print("Description cannot be blank or contain spaces. Please correct.\n")
        else:
            break

    return "{:02}".format(ch), "{:02}".format(ex), desc


def clean(str):
    """
    Cleans str, replacing invalid characters (non-letters; underscores allowed) with underscore.
    :param str: str -> string to clean
    :return: str -> cleaned string
    """
    cleaned_str = ""
    for char in str:
        if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z' or char == '_':
            cleaned_str += char
        else:
            cleaned_str += '_'

    return cleaned_str


if __name__ == '__main__':
    main()
