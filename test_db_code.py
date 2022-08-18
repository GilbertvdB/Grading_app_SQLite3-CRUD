# This file is to create the database in mySQL
# The database will hold the name of the student,
# the subjects and the grades.
# and to further test queries before implementing in main

import sqlite3



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
def column_string_length(row):
    """ Voor elke kolom van een lijst die uit tuples bestaat, wordt
    de lengte van de langste string opgeslagen in een lijst.
    :return: de maximale string lengte voor elke kolom."""
    length = len(row[0])
    len_list = [0 for _ in range(length)]
    # Vergelijk elke regel met elkaar en slaat de langste lengte op.
    x = 0
    while x < len(row[0]):
        for items in row:
            if len(str(items[x])) > len_list[x]:
                len_list[x] = len(str(items[x])) + 4  # Lengte tab is +4.
        x += 1
    return len_list


def print_format(row, num=False):
    """ Prints the columns from tuples in a list neatly spaced. With the
     option the add sequential numbers in the front by stating True as
     second argument. """
    padding = column_string_length(row)
    on = num
    # display a list of tuples neatly
    nummering = 0
    for items in row:
        string = ''
        nummering += 1
        for x in items:
            i = items.index(x)
            if x is None:  # if the element is type None
                blank = '-'
                num = f"{nummering:<1}"
                string += f'{blank:<{(padding[i])}}'
            else:
                num = f"{nummering:<1}"
                string += f'{items[i]:<{(padding[i])}}'
        if on is True:
            print(num, string)
        else:
            print(string)
    print()


def get_viewinfo_teststudent(search='off', target=None):
    if search == 'off':
        cursor.execute(f"SELECT * FROM test_student")
        rows = cursor.fetchall()
        return rows
    else:
        cursor.execute(f"SELECT * FROM test_student WHERE {search} = '{target}' ")
        rows = cursor.fetchall()
        return rows



# todo short this(db search done)
def update_grade():
    # 3 data points, class ID, Student ID, subject name
    # prompt student search
    print("--------- Grading ------------- ")
    class_name = (input("Input class name: ")).upper()
    print()

    # db search
    rows = get_viewinfo_teststudent(search='ClassName', target=class_name)
    print_format(rows, True)

    # choose student
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


def key_words(search='off', target=None):
    # def key_words(search='off', firstname=None, lastname=None, classname=None, mentor=None):
    #     lst = [firstname, lastname, classname, mentor]
    #     result = [x for x in lst if bool(x) is True]
    if search == 'off':
        print("search mode is Off")
        cursor.execute(f"SELECT * FROM test_student")
        rows = cursor.fetchall()
        return rows
    else:
        print("search mode is On.", search, target)
        cursor.execute(f"SELECT * FROM test_student WHERE {search} = '{target}' ")
        rows = cursor.fetchall()
        return rows

if __name__ == '__main__':

    update_grade()

    # rows = key_words(search='Mentor', target='Amber')
    # print_format(rows, True)


    cursor.close()
    db.close()
