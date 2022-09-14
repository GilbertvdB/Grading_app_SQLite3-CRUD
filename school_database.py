# codes for editing the school database
import sqlite3
import menu_files
from e_mail_generator import email_generator
from template_grades import main as add_temp

db = sqlite3.connect("school.db")
cursor = db.cursor()


def get_table_info(table: str):
    """ Retrieve and display all the information from a table."""
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    return rows


# dynamic version of get_table_info
def get_t_info(select='*', where='All', table=None, target=None):
    if where == 'All':
        col_names = cursor.execute(f"SELECT {select} FROM {table}")
        rows = cursor.fetchall()
        header = tuple([x[0] for x in col_names.description])  # return column names
        rows.insert(0, header)
        return rows
    else:
        col_names = cursor.execute(f"SELECT {select} FROM {table} WHERE {where} = '{target}' ")
        rows = cursor.fetchall()
        header = tuple([x[0] for x in col_names.description])
        rows.insert(0, header)
        return rows


# todo review - search get_header
def get_header(table_name: str):
    """ Gets the headers for a table. Skipping the first column. The
    id column auto increments in sql."""
    header = cursor.execute(f"SELECT * FROM '{table_name}'")
    headers = []
    x = 0
    for columns in header.description:
        # skip the id column - sql autoincrement
        if 'Id' in columns[0]:
            continue
        else:
            headers.append(columns[0])
    return tuple(headers), table_name


def prompt_info(info: tuple):
    """ Ask user for the input data for every column header in the
    tabel."""
    columns, table_name = info
    values = []
    print(table_name)
    for col in columns:
        if col == "Email":
            i = ""
            values.append(i)
        elif col == "LevelCode":
            i = input(f"{col}(ST or Te): ")
            values.append(i)
        else:
            i = input(f"{col}: ")
            values.append(i)
    return columns, tuple(values), table_name


def input_info(info):
    """Inputs the info from the tuples and adds and saves the values in
    the table database."""
    columns, values, t_name = info
    cursor.execute(f"INSERT INTO {t_name} {columns} VALUES {values} ")
    db.commit()


def get_reg_id(f_name, l_name):
    """ Gets the registry id number."""

    cursor.execute(f"SELECT RegID from Registry WHERE FirstName = '{f_name}' "
                   f"AND LastName = '{l_name}' ")
    row = cursor.fetchone()
    reg_id = row[0]
    return reg_id


def get_class_id(class_name):
    """ Gets the class id number."""
    cursor.execute(f"SELECT ClassID from Classes WHERE ClassName = '{class_name}' ")
    row = cursor.fetchone()
    class_id = row[0]
    return class_id


def update_class_registry(class_id, student_id):
    """ Updates the class registry with a class id and a student id."""
    cursor.execute(f'''INSERT INTO ClassRegistry 
    VALUES ('{class_id}', {student_id}) ''')
    db.commit()


def update_class(mentor_id, class_id):
    """ Updates the class table."""
    cursor.execute(f"UPDATE Classes SET MentorId = {mentor_id} WHERE ClassId = '{class_id}' ")
    db.commit()


def set_class(class_name, mentor_id="", year='22'):
    """ Updates the class table."""
    cursor.execute(f"INSERT INTO Classes VALUES('{year + class_name}','{class_name}','{mentor_id}')")
    db.commit()


def get_classes():
    """ Get all info from the Classes table and return the data."""
    cursor.execute("SELECT * FROM Classes")
    data = cursor.fetchall()
    return data


def add_class():
    """ Prompts user for information and adds a new class
    to the Classes table. MentorId is optional."""
    class_name = input("Enter new class name: ")
    mentor_id = input("Enter Mentor Id or press Enter to skip")
    set_class(class_name.upper(), mentor_id)


def set_grading_profile(student_id, class_id):
    """ Creates a new grading profile from a class id and student id."""
    cursor.execute(f"INSERT INTO grades_t1_2022 ('student_id', 'class_id') "
                   f"VALUES ({student_id}, '{class_id}') ")
    db.commit()


def add_to_reg():
    """ Start the registry process to add a person to the database.
    Returning the firstname of the person. """
    head = get_header('Registry')
    info = prompt_info(head)
    firstname = info[1][3]
    prefix = info[1][2]
    lastname = info[1][1]
    input_info(info)
    return firstname, lastname


def add_student():
    """ Adds a student profile in the database."""
    # start the registry process and get the FirstName
    student = add_to_reg()
    assign_class = input("Class: ")
    student_id = get_reg_id(*student)  # get studentID
    class_id = get_class_id(assign_class)  # get ClassId
    # update ClassRegistry
    update_class_registry(class_id, student_id)
    # create grading profile
    set_grading_profile(student_id, class_id)
    # create email address
    row = get_t_info(where='RegId', table='Registry', target=student_id)
    email_generator(row)
    first, last = student
    print(f"Student {first} {last} added to the database.")


def add_teacher():
    """ Adds a teacher profile to the database. """
    # start the registry process and get the FirstName
    teacher_name = add_to_reg()
    teacher_id = get_reg_id(*teacher_name)  # get teacherID
    # create email address
    row = get_t_info(where='RegId', table='Registry', target=teacher_id)
    email_generator(row)
    # mentors a class option
    class_mentor = input("Mentors a class? y/n: ")
    if class_mentor == 'y':
        assign_class = input("Mentor for class: ")
        class_id = get_class_id(assign_class)  # get ClassId
        # update Classes
        update_class(teacher_id, class_id)
    elif class_mentor == 'n':
        pass
    else:
        print("Not valid choice")
    first, last = teacher_name
    print(f"Teacher {first} {last} added to the database.")


def get_teacher_info():
    """ Gets the teacher info from a view in the database and prints it out."""
    info = get_t_info(select='FirstName, LastName, Email',
                      table='teacher_registry')
    print_format(info, head='on')


def get_student_info():
    """ Gets the student info from a view in the database and prints it out."""
    info = get_t_info(select='FirstName, LastName, ClassName as Class, Mentor',
                      table='test_student')
    print_format(info, head='on')


def column_string_length(rows):
    """ Voor elke kolom van een lijst die uit tuples bestaat, wordt
    de lengte van de langste string opgeslagen in een lijst.
    :return: de maximale string lengte voor elke kolom."""
    len_rows = len(rows)
    len_items = len(rows[0])
    len_list = [0 for _ in range(len_items)]
    # Vergelijk elke regel met elkaar en slaat de langste lengte op.
    for x in range(len_rows):
        for y in range(len_items):
            item = rows[x][y]
            if len(str(item)) + 4 > len_list[y]:
                len_list[y] = len(str(item)) + 4
    return len_list


def print_format(row, enum="off", head="off"):
    """ Prints the columns from tuples in a list neatly spaced. With the
     option the add sequential numbers in the front and or displaying the
     column headers. """
    len_list = column_string_length(row)  # list with max string lengths
    total_rows = len(row)
    l_max = len(str(total_rows))  # gets the spacing size for enumeration
    num = 1
    for items in row:
        i_length = len(items)  # total items in the tuple
        x = 0
        if head == 'off':  # skip header
            if row.index(items) == 0:
                continue
        if enum == 'on':  # enable numbering
            if head == 'on' and row.index(items) == 0:
                print((' ' * l_max).rjust(l_max) + ' ', end=' ')
            else:
                print(str(num).rjust(l_max) + '.', end=' ')
                num += 1
        while x < i_length:  # print items in the tuple with correct padding
            if items[x] is None:
                print('-'.ljust(len_list[x]), end='')
            else:
                print(str(items[x]).ljust(len_list[x]), end='')
            x += 1
        print()


def profile_display_format(lst):
    """Display table information neatly under each other. Takes a list with two tuples."""
    new_list = list(zip(lst[0], lst[1]))  # ie (RegId, 39)
    for items in new_list:
        # if new_list.index(items) == 0 or new_list.index(items) == 1:
        #     continue  # skip the first two items. (RegId and LevelCode)
        # else:
        if items[1] is None:
            print(f"{items[0] + ':':<14} - ")
        else:
            print(f"{items[0] + ':':<14}{items[1]}")


def get_stu_fullname(id_student):
    cursor.execute(f"SELECT FirstName, LastName FROM Registry WHERE RegId = {id_student} ")
    row = cursor.fetchone()
    print(*row)


# get report card with search options
def view_reportcard():
    search_string = input("Please enter student id, class or student full name: ")
    print()
    string_list = search_string.title().split(' ')  # list with names
    if search_string.isnumeric():  # student id provided.
        student_id = search_string
        get_stu_fullname(student_id)  # TODO double check - does it do something?
        print_report(student_id)
    elif len(search_string) == 2 and search_string.isalnum():  # class id prov.
        class_name = search_string.upper()
        # return students list from the class name
        rows = get_t_info(select='FirstName, Lastname, ClassName as Class, Mentor',
                          where='ClassName', table='test_student', target=class_name)
        print_format(rows, number="on", head="on")

        # choose student
        student = input("Choose student: ")
        choice = rows[int(student)]
        f_name, l_name, _, _ = choice
        student_id = get_reg_id(f_name, l_name)  # get id number
        print()
        print(f_name, l_name)
        print_report(student_id)
    elif len(string_list) > 1:  # firstname and lastname are provided.
        one_string = ''.join(string_list)
        if one_string.isalpha():
            f_name, l_name = string_list
            student_id = get_reg_id(f_name, l_name)
            print(f_name, l_name)
            print_report(student_id)
    else:
        print("Type a valid search option!")


def print_report(id_student):
    """ Display a student's reportcard by getting the grades from
      the database and printing it a viewable format."""

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


def get_subjects():
    """ Display a list of the known subjects in the database"""
    cursor.execute("SELECT * FROM Subjects")
    row = cursor.fetchall()
    return row


def view_subjects():
    subjects = get_subjects()
    print("Current Subjects: ")
    print_format(subjects, head='on')


def set_grade(id_student):
    """ Sets the grade for a student. Prompting for the subject and grade."""
    loop = "on"
    while loop == "on":
        # choose vak and grade
        vak = input("Choose a subject: ")
        vak = vak.upper()
        cijfer = input(f"Enter a grade for {vak}: ")
        print()
        # update grade
        cursor.execute(f"UPDATE grades_t1_2022 SET {vak} = '{cijfer}' WHERE student_id = {id_student} ")
        db.commit()  # confirm the changes in the database.
        # update another subject?
        choice = input("Continue updating? Y / N: ")
        if choice == 'Y' or choice == 'y':
            print()
            continue
        else:
            print()
            loop = "off"


def update_subjects():
    """ Adds a subject to the database. If it already exists lets the
    user know. If not then it adds the new subject to the database."""

    # print a list of the already known subjects
    subject_list = get_subjects()
    view_subjects()
    print()

    # prompts user for the subject name of 0 to exit.
    subject_code = (input("Add subject code or press 0 voor Exit: ")).upper()
    check = [bool(item) for item in subject_list if subject_code in item]
    while subject_code != '0':
        if bool(check) is True:  # subject already exists.
            print("Subject already exists!")
            print()
            break
        else:  # subject does not exist yet. Add to database
            subject = input("Subject name: ")
            cursor.execute(f"INSERT INTO Subjects ('SubjectCode', 'SubjectName') "
                           f"VALUES ('{subject_code}', '{subject}')")
            cursor.execute(f"ALTER TABLE grades_t1_2022 ADD {subject_code} NUMERIC")
            db.commit()  # confirm the changes in the database.
            print()
            print(f"Subject: '{subject_code}' - {subject} has been added.")
            view_subjects()  # let the user know update is complete.
            subject_code = '0'
    else:
        print()


def update_grade():
    # prompt student search by class name
    print("--------- Grading ------------- ")
    class_name = (input("Input class name: ")).upper()
    print()

    # db search
    rows = get_t_info(select='FirstName, Lastname', where='ClassName',
                      table='test_student', target=class_name)
    print_format(rows, number="on", head="on")

    # choose student
    student = input("Choose student: ")
    choice = rows[int(student)]
    # f_name, l_name, _, _ = choice
    f_name, l_name = choice[0], choice[1]

    student_id = get_reg_id(f_name, l_name)  # get id number
    print(f_name, l_name)
    print_report(student_id)
    set_grade(student_id)  # update grade
    print(f_name, l_name)
    print_report(student_id)  # update the user with the changes made.


def update_class_mentor():
    # get class mentor info
    class_mentor_info = get_t_info(select='ClassName as Class, Mentor', table='class_mentors')
    print_format(class_mentor_info, head="on")
    class_choice = input("Choose class to update: ")
    class_id = get_class_id(class_choice.upper())
    # get teacher info
    data = get_t_info(select='FirstName, LastName, RegId as Code', table='teacher_registry')
    print_format(data, number="on", head="on")
    choice = input("Choose teacher: ")
    teacher_info = data[int(choice)]
    reg_id = teacher_info[2]
    update_class(reg_id, class_id)
    print("Class mentor updated!")
    print()


def view_class_info():
    class_choice = (input("Enter a class or press enter for all: ")).upper()
    if class_choice == '':
        info = get_t_info(select='ClassName as Class, FirstName, LastName, Mentor',
                          table='test_student')
    else:
        info = get_t_info(select='ClassName as Class, FirstName, LastName, Mentor',
                          table='test_student', where='ClassName',
                          target=class_choice)
    print_format(info, head='on')


def grade_choose_trimester():
    choice_trimester = input("Choose trimester. Enter T1, T2 or T3: ").lower()
    return choice_trimester


def grade_choose_subject():
    valid_choice = False
    while valid_choice is not True:
        subject = (input("Enter a subject or press Enter for all: ")).upper()
        subject_info = get_subjects()  # exam. [(1, NE, Nederlands), ...]
        subject_list = [x[1] for x in subject_info]  # get second items
        if subject != '' and subject not in subject_list:
            print("Not a valid subject. Please try again")
        else:
            valid_choice = True  # stop evaluation and proceed
            return subject


def grade_choose_classes():
    valid_choice = False
    while valid_choice is not True:
        classes = (input("Enter a class or press Enter for all: ")).upper()
        classes_info = get_classes()  # exam. [(221A, 1A, 13), ...]
        classes_list = [x[1] for x in classes_info]  # get second items
        if classes != '' and classes not in classes_list:
            print("Not a valid class. Please try again")
        else:
            valid_choice = True  # stop evaluation and proceed
            return classes


def view_grades_all(trimester):
    row = get_t_info(table='all_grades_' + trimester + '_2022')
    print_format(row, head='on')


def grade_display_results(trimester, subject, classes):
    print("Trimester:", trimester.upper())
    if classes == '' and subject == '':
        view_grades_all(trimester)
    elif classes == '':
        row = get_t_info(select=f'{subject}', table='all_grades_' + trimester + '_2022')
        print(*[x[0] for x in row if x[0] is not None], sep='\n')
    elif subject == '':
        row = get_t_info(select='*', table='all_grades_' + trimester + '_2022',
                         where='Class', target=f'{classes}')
        print_format(row, head='on')
    else:
        row = get_t_info(select=f'{subject}', table='all_grades_' + trimester + '_2022',
                         where='Class', target=f'{classes}')
        print(*[x[0] for x in row if x[0] is not None], sep='\n')


def view_grade():
    choice_trimester = grade_choose_trimester()
    choice_subject = grade_choose_subject()
    choice_class = grade_choose_classes()
    print()
    grade_display_results(choice_trimester, choice_subject, choice_class)


def profile_search_naw():
    # person NAW
    search = input("Enter first or last name: ")
    if search == '':
        data = cursor.execute(f"SELECT Fullname as Name FROM 'fullnames_view' ")
        row = cursor.fetchall()
    else:
        data = cursor.execute(f"SELECT Fullname as Name FROM 'fullnames_view' "
                              f"WHERE LastName LIKE '%{search}%' OR FirstName LIKE '%{search}%' ")
        row = cursor.fetchall()
    print()
    header = tuple([x[0] for x in data.description])  # return column names
    row.insert(0, header)
    print_format(row, head='on', number='on')
    return row


def profile_view_info(row):
    choice = input("Choose a person by entering a number: ")
    person = row[int(choice)]
    naw = get_t_info(select='RegId', table='fullnames_view', where='FullName', target=person[0])
    reg_id = naw[1][0]
    selection = 'FirstName, Prefix, LastName, Birthdate, Address, City, PostalCode, Phone, Email'
    data = get_t_info(select=selection, table='Registry', where='RegId', target=reg_id)
    profile_display_format(data)


def view_profile():
    data = profile_search_naw()
    profile_view_info(data)
    print()

# create view class info function, updated table headers
# TODO add create view to template_grades
# TODO research table templates (q1, q2, q3, q4, finals)
# TODO teacher name codes
# todo subject profiles, taal, exact.
# todo check pivot info for subject & grades table


if __name__ == '__main__':
    rg = 'Registry'
    cl = 'Classes'
    sb = 'Subjects'

    main_menu = menu_files.main_menu
    menu_files.menus(main_menu)


    cursor.close()
    db.close()
