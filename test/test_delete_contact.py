from model.contact import Contact


def test_delete_edit(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name='test'))
    app.contact.delete()
