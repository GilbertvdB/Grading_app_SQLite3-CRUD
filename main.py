import sqlite3
from Menu import menu, sub_menu


def menus():
    print()
    print("Hoofd Menu:")
    for index, optie in enumerate(menu):
        print(f'{index + 1}: {optie}')
    print("0: Exit")
    print("-" * 20)


def submenu():
    print("Sub Menu:")
    for indx, opties in enumerate(sub_menu):
        print(f'{indx + 1}: {opties}')
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
    for column in data.description:
        print(column[0], end='|')
    print()
    print(*row)
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
    vak = input("Vak toevoegen: ")
    if vak in vak_list:
        print("Vak bestaat al!")
    else:
        cursor.execute(f"ALTER TABLE info_data2 ADD {vak} TEXT")
        print()
        print(f"Vak: `{vak}` toegevoegd.")
        db.commit()
        print_vak_list()


db = sqlite3.connect("info_data2.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS info_data2 (naam TEXT, ne TEXT, en TEXT)")
cursor = db.cursor()

# menu
while True:
    menus()

    choice = int(input("Kies een optie: "))
    print()
    if choice == 1:
        while choice == 1:
            update_grade()
            submenu()

            choice = int(input("Kies een sub optie: "))
            print()
        if choice == 0:
            break
        else:
            pass
    elif choice == 2:
        print("Rapport weergeven")
        scholier = input("Naam student: ")
        print(f"Rapport van {scholier}:")
        print("-" * 20)
        print_report()
        input("Druk op enter voor de hoofd menu.")

    elif choice == 3:
        update_vak()

    elif choice == 0:
        break

cursor.close()
db.close()
