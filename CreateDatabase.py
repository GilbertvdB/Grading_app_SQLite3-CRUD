# This file is to create the database in mySQL
# The database will hold the name of the student,
# the subjects and the grades.

import sqlite3

# checks if the database already exists otherwise creates it.
db = sqlite3.connect("info_data.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS info_data (name TEXT, vak TEXT)")

db.close()