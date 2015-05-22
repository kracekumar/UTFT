# -*- coding: utf-8 -*-

import views
import ui

from validations import BaseValidator


class DummyValidator(BaseValidator):
    MAPPING = {'name': {'required': True}}


def test_recursively_validate(capsys):
    validator = DummyValidator
    data = {'name': ''}
    names = {'name': ''}

    views.recursively_validate(validator=validator, data=data, names=names)

    # Assert it displayed errors
    # Assert reprompt
    # Assert result data is updated.
