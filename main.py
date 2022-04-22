import sqlite3
from Menu import menu, sub_menu
# from test_db_code import update_db, print_report

class Classy:
    def update_db(self):
        #TODO link the scholieren. Maybe via class.
        query = f"SELECT EXISTS(SELECT * FROM info_data2 WHERE naam = '{scholier}')"
        data_check = cursor.execute(query)
        rows = cursor.fetchone()

        for x in rows:
            if x == 0:
                # print("No Jan in data. Creating data.")
                cursor.execute(f"INSERT INTO info_data2 (naam, {vak}) VALUES ('{scholier}', '{cijfer}')")
            else:
                cursor.execute(f"UPDATE info_data2 SET {vak} = '{cijfer}' WHERE naam = '{scholier}' ")
                # print("Jan in data")

        db.commit()
        print_report()


    def print_report(self):
        data = cursor.execute("SELECT * FROM info_data2")
        cursor.execute(f"SELECT * FROM info_data2 WHERE naam = '{scholier}'")
        row = cursor.fetchone()
        for column in data.description:
            print(column[0], end='|')

        print()
        print(*row)


    def input_change(self):
        print()
        print("Cijfer Invoeren")
        print("-" * 20)
        scholier = input("Naam Scholier: ")
        vak = input("Kies vak: ")
        cijfer = input("Voer cijfer in:  ")
        print()

        update_db()
        print()


db = sqlite3.connect("info_data2.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS info_data2 (naam TEXT, ne TEXT, en TEXT)")
cursor = db.cursor()

# menu
while True:
    print("Hoofd Menu:")
    for index, optie in enumerate(menu):
        print(f'{index + 1}: {optie}')
    print("0: Exit")
    print("-" * 20)

    choice = int(input("Kies een optie: "))

    if choice == 1:
        input_change()
        # print()
        # print("Cijfer Invoeren")
        # print("-" * 20)
        # scholier = input("Naam Scholier: ")
        # vak = input("Kies vak: ")
        # cijfer = input("Voer cijfer in:  ")
        # print()
        #
        # update_db()
        # print()
#TODO after viariable link. Test if options.
        input("Press ENTER to continue...")
        print()
    elif choice == 0:
        break

cursor.close()
db.close()
