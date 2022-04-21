# This file is to create the database in mySQL
# The database will hold the name of the student,
# the subjects and the grades.
# and to further test queries before implementing in main

import sqlite3


def update_db():
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


def print_report():
    data = cursor.execute("SELECT * FROM info_data2")
    cursor.execute(f"SELECT * FROM info_data2 WHERE naam = '{scholier}'")
    row = cursor.fetchone()
    for column in data.description:
        print(column[0], end='|')

    print()
    print(*row)


# checks if the database already exists otherwise creates it.


db = sqlite3.connect("info_data2.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS info_data2 (naam TEXT, ne TEXT, en TEXT)")
cursor = db.cursor()


if __name__ == '__main__':

    scholier = 'Jan'
    vak = 'en'
    cijfer = '5.6'

    update_db()

    vak = 'ne'
    cijfer = '9.8'

    update_db()

    cursor.close()
    db.close()
