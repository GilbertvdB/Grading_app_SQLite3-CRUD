# This file is to create the database in mySQL
# The database will hold the name of the student,
# the subjects and the grades.
# and to further test queries before implementing in main

import sqlite3


db = sqlite3.connect("school.db")
cursor = db.cursor()

# modified get header
# def get_simple_header(data):
#     """ Gets the headers for a table."""
#     header = tuple([x[0] for x in data.description])
#     return header

# original
# def print_format(row, num=False):
#     """ Prints the columns from tuples in a list neatly spaced. With the
#      option the add sequential numbers in the front by stating True as
#      second argument. """
#     padding = column_string_length(row)
#     on = num
#     # display a list of tuples neatly
#     nummering = 0
#     for items in row:
#         string = ''
#         nummering += 1
#         for x in items:
#             i = items.index(x)
#             if x is None:  # if the element is type None
#                 blank = '-'
#                 num = f"{nummering:<1}."
#                 string += f'{blank:<{(padding[i])}}'
#             else:
#                 num = f"{nummering:<1}."
#                 string += f'{items[i]:<{(padding[i])}}'
#         if on is True:
#             print(num, string)
#         else:
#             print(string)
#     print()

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


def print_format(row, number="off", head="off"):
    """ Prints the columns from tuples in a list neatly spaced. With the
     option the add sequential numbers in the front by stating True as
     second argument. """
    padding = column_string_length(row)
    # display a list of tuples neatly
    numbering = 0
    for items in row:
        string = ''
        numbering += 1
        if row.index(items) == 0:
            numbering = 0
            if head == "off":
                continue
        for x in items:
            i = items.index(x)
            if x is None:  # if the element is type None
                blank = '-'
                num = f"{numbering:<1}."
                string += f'{blank:<{(padding[i])}}'
            elif row.index(items) == 0:  # header
                num = f"{' ':<1} "
                string += f'{items[i]:<{(padding[i])}}'
            else:
                num = f"{numbering:<1}."
                string += f'{items[i]:<{(padding[i])}}'
        if number == "on":
            print(num, string)
        else:
            print(string)
    print()


def print_report(id_student):
    """ Display a student's reportcard by getting the grades from
      the database and printing it a viewable format."""

    # fetch the student's grades from the database
    data = cursor.execute("SELECT * FROM grades_t1_2022")
    cursor.execute(f"SELECT * FROM grades_t1_2022 WHERE student_id = {id_student} ")
    row = cursor.fetchone()

    x = 0
    y = '\t\t'
    for column in data.description:
        if x == 0 or x == 1:
            x += 1
        else:
            print(column[0], row[x], sep=y, end='\n')
            x += 1
    print()


if __name__ == '__main__':

    # teacher_name = ('Pepper', 'Pots')
    # first, last = teacher_name
    # print(f"Teacher {first} {last} added to the database.")

    # data = [('RegId', 'LevelCode', 'LastName', 'Prefix', 'FirstName', 'Birthdate', 'Address', 'City', 'PostalCode', 'Phone', 'Email'),
    #        (39, 'ST', 'Benz', 'Der', 'Imma', '31-03-1996', 'WatchStreet 12', 'Bronx', '1010BX', None, 'd_benz@school.com')]
    #
    # def profile_display_format(lst):
    #     """Display table information neatly under each other. Takes a list with two tuples."""
    #     new_list = list(zip(lst[0], lst[1]))  # ie (RegId, 39)
    #     for items in new_list:
    #         if new_list.index(items) == 0 or new_list.index(items) == 1:
    #             continue  # skip the first two items. (RegId and LevelCode)
    #         else:
    #             if items[1] is None:
    #                 print(f"{items[0] + ':':<14} - ")
    #             else:
    #                 print(f"{items[0] + ':':<14}{items[1]}")
    #
    #
    # profile_display_format(data)

    id_student = 57
    trim_list = ['t1', 't2', 't3']
    grades_list = []
    # fetch the student's grades from the database
    data = cursor.execute("SELECT * FROM grades_t1_2022")

    for trim in trim_list:
        cursor.execute(f"SELECT * FROM grades_{trim}_2022 WHERE student_id = {id_student} ")
        row = cursor.fetchone()
        grades_list.append(row)

    x = 0
    y = '\t\t'
    print('  \t\tT1 \t\tT2 \t\tT3')
    for column in data.description:
        if x == 0 or x == 1:
            x += 1
        else:
            print(column[0], float(grades_list[0][x]), float(grades_list[1][x]),
                  float(grades_list[2][x]), sep=y, end='\n')
            x += 1
    print()



    cursor.close()
    db.close()
