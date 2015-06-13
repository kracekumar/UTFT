# -*- coding: utf-8 -*-

import unittest

import views
import cli


class ResolveTestCase(unittest.TestCase):
    def test_resolve_for_existing_action(self):
        res = cli.resolve('add')
        self.assertEquals(res, views.add)

    def test_resolve_for_missing_action(self):
        res = cli.resolve('foo')
        self.assertEqual(res, None)

    def test_resolve_for_add_with_spaces_around(self):
        res = cli.resolve(' add ')
        self.assertEquals(res, views.add)


if __name__ == "__main__":
    unittest.main()
