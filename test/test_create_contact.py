# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(name="qqq", midname="www", last_name="eee", nick="rrr", title="ttt", comp_name="yyy", address="uuu", home_number="iii", email="aaa", date="9", birth_month="September",
                               birth_year="1990"))

