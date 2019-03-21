from model.contact import Contact


def test_edit_from_hp(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name='edit_test'))
    app.contact.edit(Contact(name="qqq_e", midname="www_e", last_name="eee_e", nick="rrr_e", title="ttt_e", comp_name="yyy_e", address="uuu_e", home="iii_e", email="aaa_e", date="1", birth_month="October",
                               birth_year="1991"))


def test_edit_from_details(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name='edit_test'))
    app.contact.edit_from_details(Contact(name="qqq_e", midname="www_e", last_name="eee_e", nick="rrr_e", title="ttt_e", comp_name="yyy_e", address="uuu_e", home="iii_e", email="aaa_e", date="1", birth_month="October",
                               birth_year="1991"))



