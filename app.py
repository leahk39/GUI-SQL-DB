import database

# test2

MENU_PROMPT = """--Drink App--

Please choose one of these options:

1) Add a new drink.
2) See all drinks.
3) Find a drink by name.
4) See which flavor is best for a drink.
5) Delete drink by name
6) Show drinks in same rating range
7) Exit.

Your selection:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            prompt_add_new_drink(connection)
        elif user_input == "2":
            prompt_see_all_drinks(connection)
        elif user_input == "3":
            prompt_find_drink(connection)
        elif user_input == "4":
            prompt_find_best_flavor(connection)
        elif user_input == "5":
            prompt_delete_drink(connection)
        elif user_input == "6":
            prompt_drink_rate_range(connection)
        else:
            print("Invalid input, please try again.")


def prompt_add_new_drink(connection):
    name = input("Enter drink name: ")
    flavor = input("Enter your favorite flavor it: ")
    rating = int(input("Enter your rating score (0-100): "))

    database.add_drink(connection, name, flavor, rating)


def prompt_see_all_drinks(connection):
    drinks = database.get_all_drinks(connection)

    for drink in drinks:
        print(f"{drink[1]} ({drink[2]}) - {drink[3]}/100")

#test
def prompt_find_drink(connection):
    name = input("Enter drink name to find: ")
    drinks = database.get_drinks_by_name(connection, name)

    for drink in drinks:
        print(f"{drink[1]} ({drink[2]}) - {drink[3]}/100")


def prompt_find_best_flavor(connection):
    name = input("Enter drink name to find: ")
    best_flavor = database.get_best_flavor_for_drink(connection, name)

    print(f"The best preparation method for {name} is: {best_flavor[0]}")


def prompt_delete_drink(connection):
    name = input("Enter drink name to delete: ")
    drink_delete = database.delete_drink_by_name(connection, name)

    print("drink deleted")


def prompt_drink_rate_range(connection):
    low = input("Enter min rating to show: ")
    high = input("Enter max rating to show: ")
    drinks = database.show_drink_range(connection, low, high)

    for drink in drinks:
        print(f"{drink[1]} ({drink[2]}) - {drink[3]}/100")


menu()