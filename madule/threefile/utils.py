print(f"utils.py loaded, __name__ = {__name__}")

import helpers


def show_greeting(name):
    print(helpers.greet(name))
