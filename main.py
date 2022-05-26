"""
Author: G van der Biezen
File name: main.py

The following program lets the user, in this case a teacher,
store grades for students in a database. A grade can be added, a new
subject can be added and also the option to view a students report card.

Python versie: 3.10.2
IDE: IntelliJ IDEA Community Edition 2021.3.2
Last update: 26/05/2021
"""

import sqlite3  # library to work with sql database
from Menu import main_menu, sub_menu  # imports the menu lists


# display menu options using a list
def menu(menu_list: list):
    """ Generates a menu from a list by using the options in `menu_list`

    :param: menu_list: Name of the menu or list where options are defined.
    """

    # Display a menu in a top-down format.
    print(f"\033[4m" + "Menu" + "\033[0m")
    for index, optie in enumerate(menu_list):
        print(f'{index + 1}: {optie}')
    print("0: Exit")
    print("-" * 20)


def update_grade():
    """ Updates a students grade by asking for the details such as,
    name, subject and grade. Afterwards using the update database
     method to make the updates."""

    # defines global variables
    global scholier
    global vak
    global cijfer

    # prompts the user for the required data
    print()
    print("Cijfer Invoeren")
    print("-" * 20)
    scholier = input("Naam Scholier: ")
    vak = input("Kies vak: ")
    cijfer = input("Voer cijfer in:  ")
    print()

    # runs the method to update the database with the data
    update_db()
    print()


def update_db():
    """ Updates a student database by first checking if the student exist
    in the database. If so updates the data otherwise creates a new entry
    with the data provided. """

    # checks if the student name exists in the table.
    cursor.execute(f"SELECT EXISTS(SELECT * FROM info_data2 WHERE naam = '{scholier}')")
    rows = cursor.fetchone()
    for x in rows:
        if x == 0:  # if the data doesn't exist yet, create entry.
            cursor.execute(f"INSERT INTO info_data2 (naam, {vak}) VALUES ('{scholier}', '{cijfer}')")
        else:       # if the data already exist, update entry.
            cursor.execute(f"UPDATE info_data2 SET {vak} = '{cijfer}' WHERE naam = '{scholier}' ")

    db.commit()  # confirm the changes in the database.
    print_report()  # update the user with the changes made.


def print_report():
    """ Display a student's reportcard by getting the grades from
      the database and printing it a viewable format."""

    # fetch the student's grades from the database
    data = cursor.execute("SELECT * FROM info_data2")
    cursor.execute(f"SELECT * FROM info_data2 WHERE naam = '{scholier}'")
    row = cursor.fetchone()

    # display a horizontal layout
    # for column in data.description:
    #     print(column[0], end=' | ')
    # print()
    # print(*row)
    # print()

    # display a vertical layout
    x = 0
    y = '\t'
    for column in data.description:
        print(column[0], row[x], sep=y, end='\n')
        x += 1
        y = '\t\t'
    print()


def print_vak():
    """ Display a list of the known subjects in the database"""

    # fetch data from the database.
    data = cursor.execute("SELECT * FROM info_data2")
    # row = cursor.fetchone()

    # print the subject for the user.
    for column in data.description:  # the headers of the database.
        if column[0] != 'naam':  # skip the first header which is name.
            print(column[0], end='|')  # print the subjects.
    print()
# TODO check both functions for duplicates


def print_vak_list():
    """ Creates and displays a list of the subjects from the database to be used
    globally. """

    global vak_list  # defines global variable.
    vak_list = []   # creates an empty list.

    # fetch data from the database.
    data = cursor.execute("SELECT * FROM info_data2")
    # row = cursor.fetchone()

    # prints a list of the subjects.
    for column in data.description:     # the headers of the database.
        if column[0] != 'naam':  # skip 'naam' which is the first header.
            vak_list.append(column[0])  # add the rest to the list.
    print(*vak_list, sep=' | ')         # print the list.


def update_vak():
    """ Adds a subject to the database. If it already exists lets the
    user know. If not then it adds the new subject to the database."""

    # print a list of the already known subjects
    print("Huidige vakken")
    print_vak_list()
    print()

    # prompts user for the subject name of 0 to exit.
    new_vak = input("Vak toevoegen of 0 voor Exit: ")
    while new_vak != '0':
        if new_vak in vak_list:  # subject already exists.
            print("Vak bestaat al!")
            print()
            break
        else:  # subject does not exist yet. Add to database
            cursor.execute(f"ALTER TABLE info_data2 ADD {new_vak} TEXT")
            print()
            print(f"Vak: `{new_vak}` toegevoegd.")
            db.commit()  # confirm the changes in the database.
            print_vak_list()  # let the user know update is complete.
    else:
        print()


# connect to the database and create the table if it doesn't exist
db = sqlite3.connect("info_data2.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS info_data2 (naam TEXT, ne TEXT, en TEXT)")
cursor = db.cursor()

# menu
while True:
    menu(main_menu)

    choice = int(input("Kies een optie: "))
    print()
    if choice == 1:
        while choice != 0:
            update_grade()
            menu(sub_menu)

            choice = int(input("Kies een optie: "))
            print()
        # old code/alternate code for while choice == 1
        # if choice == 0:
        #     break
        # else:
        #     pass
    elif choice == 2:
        print("Rapport weergeven")
        scholier = input("Naam student: ")
        print()
        print(f"\033[4m" + "Rapport" + "\033[0m")
        print_report()
        input("Druk op enter voor de hoofd menu...")
        print()

    elif choice == 3:
        update_vak()

    elif choice == 0:
        break

cursor.close()
db.close()
