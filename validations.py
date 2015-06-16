# -*- coding: utf-8 -*-

from collections import defaultdict


class BaseValidator(object):
    def __init__(self, data):
        self.data = data
        self._errors = defaultdict(list)

    @property
    def errors(self):
        return self._errors

    def validate_email(self, name, val):
        if '@' not in val and '.' not in val:
            self._errors[name].append('Invalid Email')

    def validate_type(self, name, val, expected_type):
        try:
            expected_type(val)
        except ValueError:
            self._errors[name].append('Expected {} of type {}'.format(
                name, expected_type))

    def validate_all(self, mapping):
        """
        MAPPING = {
        'first_name': {'required': True, 'max': 255},
        'last_name': {'required': False, 'max': 255},
        'email': {'required': False, 'max': 255, 'is_email': True},
        'phone': {'required': True, 'max': 15}
        }
        """
        for name, value in mapping.items():
            val = self.data.get(name, '')
            if value['required']:
                if not val:
                    self.errors[name].append('Value is missing')
                elif value.get('max') and isinstance(val, basestring) and \
                     len(val) >= value['max']:
                    msg = "Max length is {}".format(value['max'])
                    self.errors[name].append(msg)

                if value.get('is_email'):
                    self.validate_email(name=name, val=val)
                if value.get('type'):
                    self.validate_type(name=name, val=val,
                                       expected_type=value.get('type'))
            else:
                if val:
                    max_len = value.get('max')
                    if max_len and isinstance(val, basestring) and \
                       len(val) >= max_len:
                        msg = "Max length is {}".format(value['max'])
                        self._errors[name].append(msg)
                    if value.get('is_email'):
                        self.validate_email(name=name, val=val)
                    if value.get('type'):
                        self.validate_type(name=name, val=val,
                                           expected_type=value.get('type'))

    def validate(self):
        self.validate_all(mapping=self.MAPPING)

    def is_valid(self):
        self.validate()
        return not bool(self._errors)


class AddValidator(BaseValidator):
    MAPPING = {
        'first_name': {'required': True, 'max': 255},
        'last_name': {'required': False, 'max': 255},
        'email': {'required': False, 'max': 255, 'is_email': True},
        'phone': {'required': True, 'max': 15}
    }


class IdValidator(BaseValidator):
    MAPPING = {'id': {'required': True, 'type': int}}
