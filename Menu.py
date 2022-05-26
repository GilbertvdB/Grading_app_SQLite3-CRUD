# here we test and modify the menu's
main_menu = ["Cijfer Invoeren",
             "Rapport",
             "Vak toevoegen"]

sub_menu = ["Nog een update maken?"
            ]

x_menu = ["optie 1",
          "optie 2",
          "optie 3",
          "optie 4"]

# menu addons for the future targeted at specific users
user_menu = ["Administrator",
             "Teacher",
             "Student"]

admin_menu = ["Vak toevoegen",
              "Placeholder"]

teacher_menu = ["Cijfer Invoeren",
                "Rapport"]

student_menu = ["Rapport"]


def menu(options: list):
    print(f"\033[4m" + "Menu" + "\033[0m")
    for index, optie in enumerate(options):
        print(f'{index + 1}: {optie}')
    print("0: Exit")
    print("-" * 20)


if __name__ == '__main__':
    # menu(main_menu)
    # menu(sub_menu)
    # menu(x_menu)

    while True:
        menu(main_menu)
        choice = int(input("Kies een optie: "))
        print()
        if choice == 1:
            while choice == 1:
                # input_change()
                menu(sub_menu)

                choice = int(input("Kies een sub optie: "))
                print()
            if choice == 0:
                break
            else:
                pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 0:
            break

    # #  Display menu style for future addons specific to users
    # while True:
    #     menu(user_menu)
    #     choice = int(input("Kies een optie: "))
    #     print()
    #     if choice == 1:
    #         while choice == 1:
    #             menu(admin_menu)
    #             choice = int(input("Kies een optie: "))
    #             print()
    #         if choice == 0:
    #             break
    #         else:
    #             pass
    #     elif choice == 2:
    #         while choice != 0:
    #             menu(teacher_menu)
    #             choice = int(input("Kies een optie: "))
    #             print()
    #             if choice == 1:
    #                 print("Cijfer Invoeren")
    #                 print()
    #             elif choice == 2:
    #                 print("Rappport weergeven")
    #                 print()
    #         else:
    #             pass
    #     elif choice == 3:
    #         menu(student_menu)
    #     elif choice == 0:
    #         break
