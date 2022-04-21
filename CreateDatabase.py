# This file is to create the database in mySQL
# The database will hold the name of the student,
# the subjects and the grades.

import sqlite3

# checks if the database already exists otherwise creates it.


def info_database():
    db = sqlite3.connect("info_data2.sqlite")
    db.execute("CREATE TABLE IF NOT EXISTS info_data2 (naam TEXT, )")

    cursor = db.cursor()
    naam = 'Jan'
    cursor.execute("INSERT INTO info_data2 (naam) VALUES(?)", (naam,))

    cursor.close()
    db.commit()
    db.close()


info_database()


