import sqlite3
from CreateDatabase import info_database

print("Rapport Systeem")
print()
print("Menu")
print("-" * 8)
print("1. Cijfer Invoeren")
print("0. Exit")

choice = input("Maak een keuze: ")

while choice != "0":
    if choice == "1":
        info_database()
        print()
        print("Cijfer Invoeren")
        print("-" * 20)
        naam = input("Naam Scholier: ")
        print(naam)
    else:
        break
