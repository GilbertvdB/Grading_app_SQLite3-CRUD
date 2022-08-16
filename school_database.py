# codes for editing the school database
import sqlite3
import menu_files


db = sqlite3.connect("school.db")
cursor = db.cursor()


def get_table_info(table: str):
    """ Retrieve and display all the information from a table."""
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    return rows


def get_header(table_name: str):
    """ Gets the headers for a table. Skipping the first column. The
    id column auto increments in sql."""
    header = cursor.execute(f"SELECT * FROM '{table_name}'")
    headers = []
    x = 0
    for columns in header.description:
        # skip the id column - sql autoincrement
        if x == 0:
            x += 1
        else:
            headers.append(columns[0])
            x += 1
    return tuple(headers), table_name


def prompt_info(info: tuple):
    """ Ask user for the input data for every column header in the
    tabel."""
    columns, t_name = info
    values = []
    print(t_name)
    for col in columns:
        i = input(f"{col}: ")
        values.append(i)
    return columns, tuple(values), t_name


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
    VALUES ({class_id}, {student_id}) ''')
    db.commit()


def update_class(mentor_id, class_id):
    """ Updates the class table."""
    cursor.execute(f"UPDATE Classes SET MentorId = {mentor_id} WHERE ClassId = {class_id} ")
    db.commit()


def set_grading_profile(student_id, class_id):
    """ Creates a new grading profile from a class id and student id."""
    cursor.execute(f"INSERT INTO Grades_q1 ('StudentId', 'ClassID') "
                   f"VALUES ({student_id}, {class_id}) ")
    db.commit()


def add_to_reg():
    """ Start the registry process to add a person to the database.
    Returning the firstname of the person. """
    head = get_header(rg)
    info = prompt_info(head)
    firstname = info[1][2]
    lastname = info[1][1]
    input_info(info)
    return firstname, lastname


def add_student():
    """ Adds a student profile in the database."""
    # start the registry process and get the FirstName
    student = add_to_reg()
    assign_class = input("Class: ")
    student_id = get_reg_id(student)  # get studentID
    class_id = get_class_id(assign_class)  # get ClassId
    # update ClassRegistry
    update_class_registry(class_id, student_id)
    # create grading profile
    set_grading_profile(student_id, class_id)


def add_teacher():
    """ Adds a teacher profile to the database. """
    # start the registry process and get the FirstName
    teacher_name = add_to_reg()
    class_mentor = input("Mentors a class? y/n: ")
    if class_mentor == 'y':
        assign_class = input("Mentor for class: ")
        teacher_id = get_reg_id(teacher_name)  # get studentID
        class_id = get_class_id(assign_class)  # get ClassId
        # update Classes
        update_class(teacher_id, class_id)
    elif class_mentor == 'n':
        pass
    else:
        print("Not valid choice")


def get_teacher_info():
    """ Gets the teacher info from a view in the database."""
    cursor.execute("SELECT * FROM teacher_registry")
    rows = cursor.fetchall()

    header, table_name = get_header('teacher_registry')
    print(header)
    # print("Name\t\t\t\t\t", "Class", "Mentor")
    column_string_length(rows)
    print_format(rows)


def get_student_info():
    """ Gets the student info from a view in the database."""
    cursor.execute("SELECT * FROM test_student")
    rows = cursor.fetchall()

    header, table_name = get_header('test_student')
    print(header)
    # for column in data.description:
    #     print(column[0], end=' ')

    print("Name\t\t\t\t\t", "Class", "Mentor")
    column_string_length(rows)
    print_format(rows)


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


def get_stu_info(id_student):
    cursor.execute(f"SELECT FirstName, LastName FROM Registry WHERE RegId = {id_student} ")
    row = cursor.fetchone()
    print(*row)


def search_query():
    search_string = input("Please enter student id, class or student name: ")
    print()
    string_list = search_string.split(' ')
    if search_string.isnumeric():
        student_id = search_string
        # return student_id
        print()
        get_stu_info(student_id)
        print_report(student_id)
    elif len(search_string) == 2 and search_string.isalnum():
        class_name = search_string.upper()
        # return classes_id
        # return student names from the class name
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

    elif len(string_list) > 1:
        one_string = ''.join(string_list)
        if one_string.isalpha():
            firstname, lastname = string_list
            cursor.execute(f"SELECT StudentID FROM class_name WHERE Firstname = '{firstname.capitalize()}' "
                           f"AND Lastname = '{lastname.capitalize()}' ")
            rows = cursor.fetchone()
            student_id = rows[0]
            get_stu_info(student_id)
            print_report(student_id)

    else:
        print("Type a valid search option!")


def get_reportcard():
    student_id = input("Please enter student id: ")
    print()
    get_stu_info(student_id)
    print_report(student_id)


def print_report(id_student):
    """ Display a student's reportcard by getting the grades from
      the database and printing it a viewable format."""

    # fetch the student's grades from the database
    data = cursor.execute("SELECT * FROM Grades_q1")
    cursor.execute(f"SELECT * FROM Grades_q1 WHERE StudentId = {id_student} ")
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


def get_subjects():
    """ Display a list of the known subjects in the database"""
    cursor.execute("SELECT * FROM Subjects")
    row = cursor.fetchall()
    return row


def view_subjects():
    subjects = get_subjects()
    print()
    print("Current Subjects: ")
    print_format(subjects)
    print()


def set_grade(id_student):
    """ Sets the grade for a student. Prompting for the subject and grade."""
    # choose vak and grade
    vak = input("Choose a subject: ")
    vak = vak.upper()
    cijfer = input(f"Enter a grade for {vak}: ")
    print()
    # update grade
    cursor.execute(f"UPDATE Grades_q1 SET {vak} = '{cijfer}' WHERE StudentID = {id_student} ")
    db.commit()  # confirm the changes in the database.


def update_subjects():
    """ Adds a subject to the database. If it already exists lets the
    user know. If not then it adds the new subject to the database."""

    # print a list of the already known subjects
    subject_list = get_subjects()
    print("Huidige vakken")
    print("Subjects: ")
    print_format(subject_list)
    print()

    # prompts user for the subject name of 0 to exit.
    subject_code = input("Vak toevoegen of 0 voor Exit: ")
    check = [bool(item) for item in subject_list if subject_code in item]
    while subject_code != '0':
        if bool(check) is True:  # subject already exists.
            print("Vak bestaat al!")
            print()
            break
        else:  # subject does not exist yet. Add to database
            subject = input("Vak naam: ")
            cursor.execute(f"INSERT INTO Subjects ('SubjectCode', 'SubjectName') "
                           f"VALUES ('{subject_code}', '{subject}')")
            cursor.execute(f"ALTER TABLE Grades_q1 ADD {subject_code} NUMERIC")
            db.commit()  # confirm the changes in the database.
            print()
            print(f"Vak: '{subject_code}' - {subject} toegevoegd.")
            print_format(get_subjects())  # let the user know update is complete.
            subject_code = '0'
    else:
        print()


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

# TODO 17/08 - compact report card view module
# TODO finish menu function addage
# TODO teacher name codes, function to update grades,
# TODO automate table info display ( add column headers)
# todo add name and headers get studentinfo
# todo finish update_grade()
# todo subject profiles, taal, exact.
# todo check pivot info for subject & grades table


if __name__ == '__main__':

    rg = 'Registry'
    cl = 'Classes'
    sb = 'Subjects'

    main = menu_files.main
    menu_files.menus(main)

    # table info check
    # for x in get_table_info(sb):
    #     print(*x)

    # head = get_header(sb)
    # info = prompt_info(head)
    # print()
    # input_info(info)

    # add_student()
    # add_teacher()
    # get_student_info()

    # update_grade()
    # print("Subjects: ")
    # print_format(get_subjects())

    # update_subjects()

    cursor.close()
    db.close()
