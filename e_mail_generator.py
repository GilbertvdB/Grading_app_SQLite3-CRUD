# an email generator
# auto creates an e-mail for newly registered persons

import sqlite3

# from school_database import get_t_info, column_string_length, print_format


db = sqlite3.connect("school.db")
cursor = db.cursor()


def generate_email(lines):
    reg_id = lines[0]
    mail = (lines[4][0] + '_' + lines[2] + '@school.com').lower()
    return mail, reg_id


def update_email_in_registry(mail, reg_id):
    cursor.execute(f"UPDATE Registry SET Email = '{mail}' WHERE RegId = {reg_id} ")
    db.commit()


def email_generator(rows):
    rows.pop(0)  # remove the header index provided by get_t_info()
    for data in rows:
        email, reg_id = generate_email(data)
        update_email_in_registry(email, reg_id)


if __name__ == '__main__':
    # Code to generate email for the whole registry list!
    # def get_table_info(table: str):
    #     """ Retrieve and display all the information from a table."""
    #     cursor.execute(f"SELECT * FROM {table}")
    #     rows = cursor.fetchall()
    #     return rows
    #
    #
    # rows = get_table_info('Registry')
    # for lines in rows:
    #     mail, reg_id = generate_email(lines)
    #     update_email_in_registry(mail, reg_id)

    cursor.close()
    db.close()
