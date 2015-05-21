# -*- coding: utf-8 -*-

import gravatar
import requests


def fecth_gravatar_url(email):
    g = gravatar.Gravatar(email)
    return g.thumb


def fetch_gravatar_image(url):
    r = requests.get(url=url)
    return r.content
