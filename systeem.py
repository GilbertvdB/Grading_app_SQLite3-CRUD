import sqlite3
# from CreateDatabase import info_database

db = sqlite3.connect("info_data2.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS info_data2 (naam TEXT, ne TEXT, en TEXT)")
cursor = db.cursor()
# menu
print("Rapport Systeem")
print()
print("Menu")
print("-" * 8)
print("1. Cijfer Invoeren")
print("0. Exit")

choice = input("Maak een keuze: ")

while choice != "0":
    if choice == "1":
        print()
        print("Cijfer Invoeren")
        print("-" * 20)
        naam = input("Naam Scholier: ")
        vak = input("Kies vak: ")
        cijfer = input("Voer cijfer in:  ")
        print(naam)

        cursor.execute("INSERT INTO info_data2 (naam, ?) VALUES(?, ?)", (vak, naam, cijfer))
        cursor.close()
        db.commit()
    else:
        break


db.close()
