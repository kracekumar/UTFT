# -*- coding: utf-8 -*-

import mock
import pytest
import views
import service
import os
import ui
import gravatar
import requests

from validations import BaseValidator


class DummyValidator(BaseValidator):
    MAPPING = {'name': {'required': True}}


@pytest.fixture
def set_env_var(request):
    os.environ['TESTING'] = '1'

    def remove_env_var():
        del os.environ['TESTING']

    request.addfinalizer(remove_env_var)


@mock.patch('ui.get_input')
def test_recursively_validate(mocked_get_input, set_env_var, capsys):
    validator = DummyValidator
    data = {'name': ''}
    names = {'name': ''}

    mocked_get_input.return_value = {'name': 'Python'}
    new_data = views.recursively_validate(validator=validator, data=data,
                                          names=names)

    mocked_get_input.assert_called_once_with(names={'name': ''})
    assert new_data == {'name': 'Python'}


class StubGravatar(object):
    def __init__(self, email):
        self.email = email
        self.thumb = 'https://foo.com/stub'


class FakeResponse(object):
    def __init__(self, content):
        self.content = content


def fake_get(url):
    if url.endswith('.py'):
        return mock.MagicMock(content='Monty Python',
                              spec_set=requests.Response)
    else:
        return mock.MagicMock(content='Normal', spec_set=requests.Response)


@mock.patch.object(gravatar, 'Gravatar', autospec=True)
@mock.patch('requests.get', autospec=True)
def test_fetch_gravatar_and_store_with_mock_stub(mocked_requests_get,
                                                 mocked_gravatar):
    mocked_gravatar.side_effect = StubGravatar
    mocked_requests_get.side_effect = fake_get

    with mock.patch('file_store.store_image') as mocked_store_image:
        mocked_store_image.return_value = '/tmp/foo.jpeg'

        res = views.fetch_gravatar_and_store(email='foo')

        mocked_requests_get.assert_called_once_with(url='https://foo.com/stub')
        mocked_gravatar.assert_called_once_with('foo')
        mocked_store_image.called

        assert mocked_store_image.call_count == 1
        assert res == '/tmp/foo.jpeg'
