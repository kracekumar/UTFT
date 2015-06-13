# -*- coding: utf-8 -*-

import os


def get_prompt():
    if os.environ.get('TESTING'):
        """
        In [41]: x = lambda y: "test"
        In [42]: x
        Out[42]: <function __main__.<lambda>>
        In [43]: x('name')
        Out[43]: 'test'
        """
        return lambda x: x
    return input
