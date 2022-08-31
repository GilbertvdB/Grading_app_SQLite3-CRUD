from school_database import *


def hello():
    print("Hello World!")


def dom():
    print("Domination!!")


user_menu = [["Administrator"],
             ["Teacher"],
             ["Student"],
             ["Test"]]

admin_menu = [["Add Student", add_student],
              ["Add Teacher", add_teacher],
              ["All Teacher Info", get_teacher_info],
              ["All Student Info", get_student_info],
              ["All Class Info", view_class_info],
              ["View Profile", view_profile],
              ["Add New Class", add_class],
              ["Update Class Mentor", update_class_mentor],
              ["View Subjects", view_subjects],
              ["Update Subjects", update_subjects],
              ["View Grades", view_grade],
              ["Update Grades", update_grade],
              ["View Report Card", view_reportcard],
              ["Dominion", dom]
              ]

teacher_menu = [["Student Info", get_student_info],
                ["Teacher Info", get_teacher_info],
                ["View Profile", view_profile],
                ["All Class Info", view_class_info],
                ["View Report Card", view_reportcard],
                ["View Subjects", view_subjects],
                ["Update Grade", update_grade]
                ]

student_menu = [["Rapport - Dominion", dom],
                ["View Report Card", view_reportcard],
                ["View Profile", view_profile],
                ]

test_menu = [["Helo", hello], ["Dominion", dom]]

main_menu = [user_menu, admin_menu, teacher_menu, student_menu, test_menu]
# main_menu = [test_user_menu, test_menu]  # for testing


def display_menu(options: list):
    print(f"\033[4m" + "Menu" + "\033[0m")
    for index, optie in enumerate(options):
        print(f'{index + 1}: {optie[0]}')
    print("0: Exit")
    print("-" * 20)


# todo - continue with menu
def menus(menu_list: list):
        global mn
        main = menu_list
        x = y = 0
        level = "user_menu"
        # main_menu
        mn = main[x]
        display_menu(mn)
        choice = input("Choose an option: ")
        x = int(choice)
        print()
        if x == 0:
            pass
        y = x
        mn = main[y]
        display_menu(mn)
        level = "user_sub_menu"
        while True:

            choice = input("Choose an option: ")
            x = int(choice)
            print()

            if x == 0:
                break
            else:
                main[y][x - 1][1]()  # run function

            data = input("press `y` to continue or press Enter to exit: ")
            if data == 'Y' or data == 'y':
                print()
                display_menu(mn)
            else:
                break
            # if isinstance(data, str) is True:
            #     pass


if __name__ == '__main__':

    # print(main_menus)

    # print(main[0][3])   # Test
    # print(main[0][0])   # administrator

    menus(main_menu)
