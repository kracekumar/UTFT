# -*- coding: utf-8 -*-

import time
import os


def store_image(content):
    name = "{name}.{ext}".format(name=str(time.time()).replace('.', ''),
                                 ext='jpeg')
    with open(name, 'w') as f:
        f.write(content)
    return os.path.abspath(name)
