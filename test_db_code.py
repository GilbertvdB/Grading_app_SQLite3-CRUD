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


if __name__ == '__main__':

    teacher_name = ('Pepper', 'Pots')
    first, last = teacher_name
    print(f"Teacher {first} {last} added to the database.")

    cursor.close()
    db.close()
