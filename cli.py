# -*- coding: utf-8 -*-

import sys

import views


ACTION_MAPPER = {
    'add': views.add,
    'display_all': views.display_all,
    'display_one': views.display_one,
}


def main():
    allowed_actions = ["add|display_one|display_all"]

    args = sys.argv
    if len(args) == 1:
        print("python cli.py {}".format(allowed_actions))
        exit(1)
    else:
        action = args[1].strip()
        func = ACTION_MAPPER.get(action)
        if func:
            func()
        else:
            print("Unknown action {}".format(action))
            exit(1)


if __name__ == "__main__":
    main()
