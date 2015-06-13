# -*- coding: utf-8 -*-

from datetime import datetime

import os


def get_name():
    name = str(datetime.now()).replace('-', '').replace(' ', '').replace(':', '')
    return name


def store_image(content):
    name = get_name()
    full_name = "{name}.{ext}".format(name=name, ext='jpeg')
    with open(full_name, 'w') as f:
        f.write(content)
    return os.path.abspath(full_name)
