# This file is to create the database in mySQL
# The database will hold the name of the student,
# the subjects and the grades.
# and to further test queries before implementing in main

import sqlite3
from school_database import *


db = sqlite3.connect("school.db")
cursor = db.cursor()


# def search_query(search_string):
#     string_list = search_string.split(' ')
#     if search_string.isnumeric():
#         student_id = search_string
#         return student_id
#     elif len(search_string) == 2 and search_string.isalnum():
#         classes_id = search_string.upper()
#         return classes_id
#     elif len(string_list) > 1:
#         one_string = ''.join(string_list)
#         if one_string.isalpha():
#             return string_list
#     else:
#         print("Type a valid search option!")

# todo short this
def update_grade():
    # 3 data points, class ID, Student ID, subject name
    # prompt student search
    print("--------- Grading ------------- ")
    class_name = input("Input class name: ")
    print()

    if class_name != '':
        class_name = class_name.upper()
        cursor.execute(f"SELECT * FROM test_student WHERE ClassName = '{class_name}' ")
        rows = cursor.fetchall()
    else:
        cursor.execute(f"SELECT * FROM test_student")
        rows = cursor.fetchall()

    print_format(rows, True)

    # choose student
    print()
    student = input("Choose student: ")
    choice = rows[int(student) - 1]
    f_name, l_name, c_name, _ = choice

    # get id number
    id_student = get_reg_id(f_name, l_name)

    # display grades for student
    print()
    print("Name: ", f_name, l_name)
    print("Class: ", c_name)
    print_report(id_student)
    set_grade(id_student)  # update grade
    print_report(id_student)  # update the user with the changes made.

if __name__ == '__main__':

    update_grade()


    cursor.close()
    db.close()
