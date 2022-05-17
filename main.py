"""
Author: G van der Biezen
File name: main.py

The following program lets the user, in this case a teacher,
store grades for students in a database. A grade can be added, a new
subject can be added and also the option to view a students report card.

Python versie: 3.10.2
IDE: IntelliJ IDEA Community Edition 2021.3.2
Last update: 17/05/2021
"""

import sqlite3  # library to work with sql database
from Menu import main_menu, sub_menu  # imports the menu lists


# display menu options using a list
def menu(menu_list: list):
    """ Generates a menu from a list by using the options in `menu_list`

    :param menu_list: Name of the menu or list where options are defined.
    """
    print(f"\033[4m" + "Menu" + "\033[0m")
    for index, optie in enumerate(menu_list):
        print(f'{index + 1}: {optie}')
    print("0: Exit")
    print("-" * 20)


def update_grade():
    # gets the data that needs to be updated
    global scholier
    global vak
    global cijfer

    print()
    print("Cijfer Invoeren")
    print("-" * 20)
    scholier = input("Naam Scholier: ")
    vak = input("Kies vak: ")
    cijfer = input("Voer cijfer in:  ")
    print()

    update_db()
    print()


def update_db():
    # checks if the data exists in the table.
    cursor.execute(f"SELECT EXISTS(SELECT * FROM info_data2 WHERE naam = '{scholier}')")
    rows = cursor.fetchone()

    # action based on True 1 or False 0
    for x in rows:
        if x == 0:
            cursor.execute(f"INSERT INTO info_data2 (naam, {vak}) VALUES ('{scholier}', '{cijfer}')")
        else:
            cursor.execute(f"UPDATE info_data2 SET {vak} = '{cijfer}' WHERE naam = '{scholier}' ")

    db.commit()
    print_report()


def print_report():
    # prints a report after updating data
    data = cursor.execute("SELECT * FROM info_data2")
    cursor.execute(f"SELECT * FROM info_data2 WHERE naam = '{scholier}'")
    row = cursor.fetchone()
    # horizontal layout
    # for column in data.description:
    #     print(column[0], end=' | ')
    # print()
    # print(*row)
    # print()

    # vertical layout
    x = 0
    y = '\t'
    for column in data.description:
        print(column[0], row[x], sep=y, end='\n')
        x += 1
        y = '\t\t'
    print()


def print_vak():
    data = cursor.execute("SELECT * FROM info_data2")
    row = cursor.fetchone()
    for column in data.description:
        if column[0] != 'naam':
            print(column[0], end='|')
    print()


def print_vak_list():
    global vak_list
    vak_list = []
    data = cursor.execute("SELECT * FROM info_data2")
    row = cursor.fetchone()
    for column in data.description:
        if column[0] != 'naam':
            vak_list.append(column[0])
    print(*vak_list, sep=' | ')


def update_vak():
    print("Huidige vakken")
    print_vak_list()
    print()
    vak = input("Vak toevoegen of 0 voor Exit: ")
    while vak != '0':
        if vak in vak_list:
            print("Vak bestaat al!")
            print()
        else:
            cursor.execute(f"ALTER TABLE info_data2 ADD {vak} TEXT")
            print()
            print(f"Vak: `{vak}` toegevoegd.")
            db.commit()
            print_vak_list()
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
