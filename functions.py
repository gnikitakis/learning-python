def unlimited_arguments(*args, **keyword_args):
    print(f"args {args}")
    for argument in args:
        print(argument)

    print(f"keyword_args {keyword_args}")
    for key in keyword_args:
        print(key)


unlimited_arguments(1, 2, 3, 4, name="Max", age=29)
