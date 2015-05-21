# -*- coding: utf-8 -*-

import sqlite3


conn = sqlite3.connect("phonebook.db")


def add(data):
    cur = conn.cursor()
    cur.execute("insert into phonebook {} values {}".format(
        tuple(data.keys()), tuple(data.values())))
    conn.commit()


def all():
    cur = conn.cursor()
    results = cur.execute("select * from phonebook")
    return results


def one(id):
    cur = conn.cursor()
    cur.execute("select * from phonebook where id=?", (id,))
    return cur.fetchone()
