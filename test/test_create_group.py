# -*- coding: utf-8 -*-

from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(name="name", header="dfzdg", footer="bgdhg"))



