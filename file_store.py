# -*- coding: utf-8 -*-

<<<<<<< HEAD
from datetime import datetime
=======
import datetime
>>>>>>> master
import os


def get_name():
<<<<<<< HEAD
    name = str(datetime.now()).replace('-', '').replace(' ', '').replace(':', '')
    return name


def store_image(content):
    name = get_name()
    full_name = "{name}.{ext}".format(name=name, ext='jpeg')
    with open(full_name, 'w') as f:
=======
    return str(datetime.datetime.now()).replace('.', '').replace(' ', '')


def store_image(content):
    name = "{name}.{ext}".format(name=str(get_name()).replace('.', ''),
                                 ext='jpeg')
    with open(name, 'w') as f:
>>>>>>> master
        f.write(content)
    return os.path.abspath(full_name)
