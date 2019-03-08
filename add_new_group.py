# -*- coding: utf-8 -*-
from application import Application
import pytest
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.stop)
    return fixture


def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_info(Group(name="name", header="dfzdg", footer="bgdhg"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_info(Group(name="", header="", footer=""))
    app.logout()

