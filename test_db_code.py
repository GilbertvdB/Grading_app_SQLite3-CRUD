# This file is to create the database in mySQL
# The database will hold the name of the student,
# the subjects and the grades.
# and to further test queries before implementing in main

import sqlite3

db = sqlite3.connect("school.db")
cursor = db.cursor()


def search_query(search_string):
    string_list = search_string.split(' ')
    if search_string.isnumeric():
        student_id = search_string
        return student_id
    elif len(search_string) == 2 and search_string.isalnum():
        classes_id = search_string.upper()
        return classes_id
    elif len(string_list) > 1:
        one_string = ''.join(string_list)
        if one_string.isalpha():
            return string_list


    else:
        print("Type a valid search option!")



if __name__ == '__main__':

    input_string = input("Please enter student id, class or student name: ")
    print()

    print(search_query(input_string))

    cursor.close()
    db.close()
