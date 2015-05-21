# -*- coding: utf-8 -*-

import db
import ui
import service
import file_store
from validations import AddValidator, IdValidator


def recursively_validate(validator, data, names):
    new_data = data.copy()
    while True:
        v = validator(data=new_data)
        if v.is_valid():
            break
        else:
            ui.display_block_sep()
            ui.display_errors(errors=v.errors)
            ui.display_block_sep()
            missing_names = {name: names[name] for name in v.errors}
            d = ui.get_input(names=missing_names)
            new_data.update(d)
    return new_data


def add():
    NAMES = {'first_name': 'First Name:', 'last_name': 'Last Name:',
             'email': 'Email:', 'phone': 'Phone:'}
    user_data = ui.get_input(names=NAMES)
    data = recursively_validate(validator=AddValidator, data=user_data, names=NAMES)
    email = data.get('email')
    if email:
        gravatar_url = service.fecth_gravatar_url(email=email)
        content = service.fetch_gravatar_image(url=gravatar_url)
        path = file_store.store_image(content=content)
        data['thumbnail_path'] = path
    db.add(data=data)
    ui.add()


def display_all():
    data = db.all()
    ui.display_all(data=data)


def display_one():
    names = {'id': 'Id:'}
    user_data = ui.get_input(names=names)
    cleaned_data = recursively_validate(validator=IdValidator,
                                        data=user_data,
                                        names=names)
    db_data = db.one(id=cleaned_data['id'])
    ui.display_one(item=db_data)
