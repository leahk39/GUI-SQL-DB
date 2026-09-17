import database

# test3
print("test")

MENU_PROMPT = """--Vinyl Store--

Please choose one of these options:

1) Add a new vinyl.
2) See all vinyls.
3) Find a vinyl by name.
4) See which album is best for a vinyl.
5) Delete vinyl by name
6) Show vinyls in same rating range
7) Exit.

Your selection:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            prompt_add_new_vinyl(connection)
        elif user_input == "2":
            prompt_see_all_vinyls(connection)
        elif user_input == "3":
            prompt_find_vinyl(connection)
        elif user_input == "4":
            prompt_find_best_album(connection)
        elif user_input == "5":
            prompt_delete_vinyl(connection)
        elif user_input == "6":
            prompt_vinyl_rate_range(connection)
        else:
            print("Invalid input, please try again.")


def prompt_add_new_vinyl(connection):
    name = input("Enter vinyl name: ")
    album = input("Enter album name: ")
    rating = int(input("Enter your rating score (0-100): "))

    database.add_vinyl(connection, name, album, rating)


def prompt_see_all_vinyls(connection):
    vinyls = database.get_all_vinyls(connection)

    for vinyl in vinyls:
        print(f"{vinyl[1]} ({vinyl[2]}) - {vinyl[3]}/100")

#test
def prompt_find_vinyl(connection):
    name = input("Enter vinyl name to find: ")
    vinyls = database.get_vinyls_by_name(connection, name)

    for vinyl in vinyls:
        print(f"{vinyl[1]} ({vinyl[2]}) - {vinyl[3]}/100")


def prompt_find_best_album(connection):
    name = input("Enter vinyl name to find: ")
    best_album = database.get_best_album_for_vinyl(connection, name)

    print(f"The best album for {name} is: {best_album[0]}")


def prompt_delete_vinyl(connection):
    name = input("Enter vinyl name to delete: ")
    vinyl_delete = database.delete_vinyl_by_name(connection, name)

    print("vinyl deleted")


def prompt_vinyl_rate_range(connection):
    low = input("Enter min rating to show: ")
    high = input("Enter max rating to show: ")
    vinyls = database.show_vinyl_range(connection, low, high)

    for vinyl in vinyls:
        print(f"{vinyl[1]} ({vinyl[2]}) - {vinyl[3]}/100")


menu()