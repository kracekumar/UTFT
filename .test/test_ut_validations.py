# -*- coding: utf-8 -*-

from validations import BaseValidator, AddValidator, IdValidator


class TestBaseValidator:
    def test_validate_invalid_email(self):
        data = {'email': 'Kracekumar'}
        validator = BaseValidator(data=data)
        validator.validate_email(name='email', val=data['email'])

        assert 'email' in validator.errors

    def test_validate_valid_email(self):
        data = {'email': 'me@kracekumar.com'}
        validator = BaseValidator(data=data)
        validator.validate_email(name='email', val=data['email'])

        assert not validator.errors

    def test_validate_type_with_mismatching_type(self):
        data = {'name': 'id', 'val': 'foo', 'expected_type': int}

        validator = BaseValidator(data=data)
        validator.validate_type(**data)

        assert 'id' in validator.errors
        assert 'type' in validator.errors['id'][0]

    def test_validate_type_with_matching_type(self):
        data = {'name': 'id', 'val': '23', 'expected_type': int}

        validator = BaseValidator(data=data)
        validator.validate_type(**data)

        assert not validator.errors


class TestAddValidator:
    def test_is_valid_with_valid_data(self):
        data = {'first_name': 'krace', 'last_name': '', 'email': '',
                'phone': 23}

        validator = AddValidator(data=data)

        assert validator.is_valid()

    def test_is_valid_with_missing_data(self):
        data = {'first_name': 'krace', 'last_name': '', 'email': '',
                'phone': ''}

        validator = AddValidator(data=data)

        assert not validator.is_valid()
