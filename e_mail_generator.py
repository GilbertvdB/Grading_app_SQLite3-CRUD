# an email generator
# auto creates an e-mail for newly registered persons

import sqlite3
# from school_database import get_table_info, column_string_length, print_format


db = sqlite3.connect("school.db")
cursor = db.cursor()


def generate_email(lines):
    reg_id = lines[0]
    mail = (lines[3][0] + '_' + lines[2] + '@school.com').lower()
    return mail, reg_id


def update_email_in_registry(mail, reg_id):
    cursor.execute(f"UPDATE Registry SET Email = '{mail}' WHERE RegId = {reg_id} ")
    db.commit()


def email_generator(rows):
    for data in rows:
        email, reg_id = generate_email(data)
        update_email_in_registry(email, reg_id)



if __name__ == '__main__':

    # rows = get_table_info('Registry')
    # for lines in rows:
    #     mail, reg_id = generate_email(lines)
    #     update_email_in_registry(mail, reg_id)

    # table = 'Registry'
    # reg = 22
    #
    # cursor.execute(f"SELECT * FROM {table} WHERE RegId = {reg}")
    # row = cursor.fetchall()
    # print(row)
    # for lines in row:
    #     mail, reg_id = generate_email(lines)
    #     update_email_in_registry(mail, reg_id)

    # mail = 'aloha'
    # reg_id = 1
    #
    # cursor.execute(f"UPDATE Registry SET Email = {mail} WHERE RegId = {reg_id} ")
    # db.commit()


    cursor.close()
    db.close()