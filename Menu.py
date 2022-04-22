# here we test and modify the menu's
menu = ["Cijfer Invoeren",
        "Tweede optie"]

sub_menu = ["Nog een update maken?",
            "Hoofd Menu"]

if __name__ == '__main__':
    # print(enumerate(menu))

    # print("Rapport Systeem")
    # print()
    # print("Menu")
    # print("-" * 8)
    # print("1. Cijfer Invoeren")
    # print("0. Exit")
    #
    # choice = input("Maak een keuze: ")

    while True:
        print("Hoofd Menu:")
        for index, optie in enumerate(menu):
            print(f'{index + 1}: {optie}')
        print("0: Exit")
        print("-" * 20)

        choice = int(input("Kies een optie: "))

        if choice == 1:
            print()
            print("Cijfer Invoeren")
            print("-" * 20)
            scholier = input("Naam Scholier: ")
            vak = input("Kies vak: ")
            cijfer = input("Voer cijfer in:  ")
            print()
        elif choice == 0:
            break
        #
        # print("Sub Menu:")
        # for index, optie in enumerate(sub_menu):
        #     print(f'{index + 1}: {optie}')
        # print("0: Exit")
        # print("-" * 20)
        #
        # choice = int(input("Kies een optie: "))

