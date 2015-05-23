# -*- coding: utf-8 -*-

import sqlite3

import os


def get_conn():
    if os.environ.get('TESTING'):
        return sqlite3.connect("test.db")
    return sqlite3.connect("phonebook.db")


def add(data):
    conn = get_conn()
    cur = conn.cursor()
    # insert into phonebook (name, phone) values (1, 2)
    cur.execute("insert into phonebook {} values {}".format(
        tuple(data.keys()), tuple(data.values())))
    conn.commit()


def all():
    conn = get_conn()
    cur = conn.cursor()
    results = cur.execute("select * from phonebook")
    return results


def one(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from phonebook where id=?", (id,))
    return cur.fetchone()
