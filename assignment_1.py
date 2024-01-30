name = input("Give me your name: ")
age = input("Give me your age: ")


def print_personal_info(name, age):
    print("Name: " + name + " Age:" + age)


def print_info(a, b):
    print(a + " " + b)


def calculate_decades_already_lived(age):
    decades = int(age / 10)
    return decades


print_personal_info(name, age)
print_info(name, age)
print(calculate_decades_already_lived(int(age)))
