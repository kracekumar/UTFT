# -*- coding: utf-8 -*-

import os


def get_prompt():
    """Return the prompt for entering input. If the environment is testing
    return echo prompt.
    """
    if os.environ.get('TESTING'):
        """
        In [41]: x = lambda y: y
        In [42]: x
        Out[42]: <function __main__.<lambda>>
        In [43]: x('test')
        Out[43]: 'test'
        """
        return lambda x: x
    return raw_input
