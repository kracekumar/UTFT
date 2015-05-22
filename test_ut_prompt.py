# -*- coding: utf-8 -*-

import os

from types import LambdaType
from prompt import get_prompt


def test_get_prompt_for_testing():
    os.environ['TESTING'] = 'True'
    prompt = get_prompt()

    assert isinstance(prompt, LambdaType)

    del os.environ['TESTING']


def test_get_prompt():
    prompt = get_prompt()

    f = raw_input
    assert prompt == f


def test_get_prompt_for_testing_read():
    os.environ['TESTING'] = 'True'
    prompt = get_prompt()

    res = prompt("name")

    assert res == "name"
