# functions to create a template for grades tables

import sqlite3

db = sqlite3.connect("school.db")
cursor = db.cursor()

# numeric
# def create_table(table_name):
#     cursor.execute(f" CREATE TABLE '{table_name}' (class_id STRING NOT NULL, student_id INTEGER NOT NULL,"
#                    f"NE NUMERIC,EN NUMERIC, SP NUMERIC, DE NUMERIC, BI NUMERIC, SK NUMERIC, IT NUMERIC,"
#                    f" WI NUMERIC, NA NUMERIC, PRIMARY KEY (class_id, student_id));")


# STRING
def create_table(table_name):
    cursor.execute(f" CREATE TABLE '{table_name}' (class_id STRING NOT NULL, student_id INTEGER NOT NULL,"
               f"NE STRING,EN STRING, SP STRING, DE STRING, BI STRING, SK STRING, IT STRING,"
               f" WI STRING, NA STRING, PRIMARY KEY (class_id, student_id));")


def copy_info(table_name):
    # - copy student and class info into the database
    # get info
    cursor.execute(f"SELECT ClassId, StudentId FROM ClassRegistry")
    row = cursor.fetchall()
    # update
    for class_id, student_id in row:
        cursor.execute(f"INSERT INTO '{table_name}' ('class_id', 'student_id') "
                       f"VALUES ('{class_id}', '{student_id}')")


def main():
    table_name = input("Enter table name: ")
    create_table(table_name)
    copy_info(table_name)
    db.commit()


if __name__ == '__main__':

    main()

    # # --- create a template
    # table_name = 'grades_t2_2022'
    #
    # # create the table
    # cursor.execute(f" CREATE TABLE '{table_name}' (class_id STRING NOT NULL, student_id INTEGER NOT NULL,"
    #                f"NE NUMERIC,EN NUMERIC, SP NUMERIC, DE NUMERIC, BI NUMERIC, SK NUMERIC, IT NUMERIC,"
    #                f" WI NUMERIC, NA NUMERIC, PRIMARY KEY (class_id, student_id));")
    #
    # # - copy student and class info into the database
    # # get info
    # cursor.execute(f"SELECT ClassId, StudentId FROM ClassRegistry")
    # row = cursor.fetchall()
    # # update
    # for class_id, student_id in row:
    #     cursor.execute(f"INSERT INTO '{table_name}' ('class_id', 'student_id') "
    #                    f"VALUES ('{class_id}', '{student_id}')")
    # db.commit()
    # # --- END

    cursor.close()
    db.close()