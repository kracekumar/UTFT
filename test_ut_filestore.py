# -*- coding: utf-8 -*-


import mock

import file_store


@mock.patch('file_store.get_name')
def test_store_image(mocked_get_name):
    mocked_get_name.return_value = '28'

    path = file_store.store_image(content='foo')

    assert path.endswith('28.jpeg')
