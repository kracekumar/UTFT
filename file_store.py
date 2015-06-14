# -*- coding: utf-8 -*-

import datetime
import os


def get_name():
    return str(datetime.datetime.now()).replace('.', '').replace(' ', '').replace(':', '').replace('-', '')


def store_image(content):
    name = "{name}.{ext}".format(name=str(get_name()), ext='jpeg')
    with open(name, 'w') as f:
        f.write(content)
    return os.path.abspath(name)
