import unittest
import sys

import pytest

import views
import cli


class ResolveTestCase(unittest.TestCase):
    def test_resolve_for_existing_action(self):
        res = cli.resolve('add')
        assert res == views.add

    def test_resolve_for_missing_action(self):
        res = cli.resolve('foo')
        assert not res

    def test_resolve_for_add_with_spaces_around(self):
        res = cli.resolve(' add ')
        assert res == views.add


class TestMain(object):
    def test_cli_called_without_args(self, capsys):
        sys.argv = ['cli.py']
        with pytest.raises(SystemExit):
            cli.main()

        assert 'cli.py' in capsys.readouterr()[0]

    def test_cli_called_with_wrong_arg(self, capsys):
        sys.argv = ['cli.py', 'foo']
        with pytest.raises(SystemExit):
            cli.main()

        assert 'Unknown' in capsys.readouterr()[0]
