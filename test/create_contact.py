# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.stop)
    return fixture


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="qqq", midname="www", last_name="eee", nick="rrr", title="ttt", comp_name="yyy", address="uuu", home_number="iii", email="aaa", date="9", birth_month="September",
                               birth_year="1990"))
    app.session.logout()

