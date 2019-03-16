
def test_delete_edit(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_from_edit()
    app.session.logout()


def test_delete_details(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_from_details()
    app.session.logout()