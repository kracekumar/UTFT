# -*- coding: utf-8 -*-

import os
import pytest
import ui


class TestDisplayField:
    @pytest.fixture
    def set_env_var(self, request):
        os.environ['TESTING'] = '1'

        def remove_env_var():
            del os.environ['TESTING']

        request.addfinalizer(remove_env_var)

    def test_display_field(self, set_env_var):
        val = ui.display_field('name')

        assert val == 'name'
