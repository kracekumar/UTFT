# -*- coding: utf-8 -*-

import pytest
import os
import unittest
import subprocess

import db


def create_test_db():
    os.environ['TESTING'] = '1'
    conn = db.get_conn()
    cur = conn.cursor()
    cur.execute(open('phonebook.sql').read())
    conn.commit()


def destroy_test_db():
    del os.environ['TESTING']
    subprocess.Popen(['rm', 'test.db'])


class TestAdd(unittest.TestCase):
    def setUp(self):
        create_test_db()

    def test_add(self):
        data = {'first_name': 'krace', 'phone': 34}
        db.add(data)

    def tearDown(self):
        destroy_test_db()


@pytest.fixture
def add_records(request):
    create_test_db()
    for i in range(10):
        data = {'first_name': 'Name {}'.format(i), 'phone': i}
        db.add(data)

    request.addfinalizer(destroy_test_db)


def test_all(add_records):
    results = db.all()
    assert len(results.fetchall()) == 10


@pytest.mark.usefixtures("add_records")
class TestOne:
    def test_one(self):
        res = db.one(id=1)

        assert res[0] == 1
