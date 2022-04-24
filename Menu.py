# here we test and modify the menu's
menu = ["Cijfer Invoeren",
        "Rapport",
        "Vak toevoegen"]


sub_menu = ["Nog een update maken?",
            "Hoofd Menu"]


def menus():
    print("Hoofd Menu:")
    for index, optie in enumerate(menu):
        print(f'{index + 1}: {optie}')
    print("0: Exit")
    print("-" * 20)


def submenu():
    print("Sub Menu:")
    for indx, opties in enumerate(sub_menu):
        print(f'{indx + 1}: {opties}')
    print("0: Exit")
    print("-" * 20)


if __name__ == '__main__':

    while True:
        menus()

        choice = int(input("Kies een optie: "))
        print()
        if choice == 1:
            while choice == 1:
                # input_change()
                submenu()

                choice = int(input("Kies een sub optie: "))
                print()
            if choice == 0:
                break
            else:
                pass
        elif choice == 2:
            print("Rapport weergeven")
            scholier = input("Naam student: ")
            print(scholier)
            print_report()
        elif choice == 3:
            pass
        elif choice == 0:
            break


