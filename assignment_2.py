names = []


def get_user_choice():
    user_input = input("You choice: ")
    return user_input


def get_name():
    name = input("Give me a name: ")
    names.append(name)


def print_names():
    print("\nList names longer than 5 characters:")
    for name in names:
        length = len(name)
        include_letter_n = "n" in name or "N" in name
        if length > 5:
            print(
                "Name: "
                + name
                + ", Length: "
                + str(length)
                + ", Includes n or N: "
                + str(include_letter_n)
            )


def empty_names_list():
    while True:
        if len(names) == 0:
            break
        names.pop()

    print("List is empty now")
    return


wait_for_input = True

while wait_for_input:
    print("Please choose:")
    print("1: Add a new name")
    print("2: Print names")
    print("e: Empty list")
    print("q: Quit")
    user_choice = get_user_choice()

    if user_choice == "1":
        get_name()
    elif user_choice == "2":
        print_names()
    elif user_choice == "q":
        wait_for_input = False
    elif user_choice == "e":
        empty_names_list()
    else:
        print("Input was invalid")
    print("-" * 20 + "\n")

print("Done!")
