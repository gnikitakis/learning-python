# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
people = [
    {"name": "Max", "age": 20, "hobbies": ["football", "basketball"]},
    {"name": "Ann", "age": 25, "hobbies": ["football", "basketball", "tennis"]},
    {"name": "Jj", "age": 28, "hobbies": ["tennis"]},
]
print(people)

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [el["name"] for el in people]
print(names)

# 3) Use a list comprehension to check whether all persons are older than 20.
check_by_age = all([el["age"] > 20 for el in people])
print(check_by_age)

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
copy_people = [el.copy() for el in people]
copy_people[0]["name"] = "Maaaaaaaaaaaax"
print(people)

# 5) Unpack the persons of the original list into different variables and output these variables.
(
    a,
    b,
    c,
) = people
print(a)
print(b)
print(c)
