# -*- coding: utf-8 -*-

import pytest
import os

from types import LambdaType
from prompt import get_prompt


@pytest.fixture
def manage_env(request):
    def setup():
        os.environ['TESTING'] = 'True'

    def teardown():
        del os.environ['TESTING']

    setup()
    request.addfinalizer(teardown)


def test_get_prompt_for_testing(manage_env):
    prompt = get_prompt()

    assert isinstance(prompt, LambdaType)


def test_get_prompt():
    prompt = get_prompt()

    f = input
    assert prompt == f


def test_get_prompt_for_testing_read(manage_env):
    prompt = get_prompt()

    res = prompt("name")

    assert res == "name"
