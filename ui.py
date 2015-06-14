# -*- coding: utf-8 -*-

from prompt import get_prompt


def display_block_sep():
    print('#' * 80)


def display_field(display_name):
    """Display the field and the value from the user.
    """
    prompt = get_prompt()
    return prompt(display_name).strip()


def get_input(names):
    """For given a list of fields get the values from the user.
    """
    return {name: display_field(display_name)
            for name, display_name in names.items()}


def display_errors(errors):
    for name, val in errors.items():
        print("{}:{}".format(name, val))


def display_item(item):
    print("Id: {}".format(item[0]))
    print("First Name: {}".format(item[1]))
    print("Last Name: {}".format(item[2]))
    print("Email: {}".format(item[3]))
    print("Thumbnail Path: {}".format(item[4]))
    print("Phone: {}".format(item[5]))


def add():
    """Get inputs from user about new fields.
    """
    print("Record added")


def display_all(data):
    display_block_sep()
    for item in data:
        display_item(item=item)
        display_block_sep()


def display_one(item):
    if item:
        display_block_sep()
        display_item(item)
        display_block_sep()
    else:
        print("Record not found")
