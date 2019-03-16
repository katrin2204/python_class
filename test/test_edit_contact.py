from model.contact import Contact


def test_edit_from_hp(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(name="qqq_e", midname="www_e", last_name="eee_e", nick="rrr_e", title="ttt_e", comp_name="yyy_e", address="uuu_e", home_number="iii_e", email="aaa_e", date="1", birth_month="October",
                               birth_year="1991"))
    app.session.logout()


def test_edit_from_details(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_from_details(Contact(name="qqq_e", midname="www_e", last_name="eee_e", nick="rrr_e", title="ttt_e", comp_name="yyy_e", address="uuu_e", home_number="iii_e", email="aaa_e", date="1", birth_month="October",
                               birth_year="1991"))
    app.session.logout()



