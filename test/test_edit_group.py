from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="name_edited", header="edited_header", footer="edited_footer"))
    app.session.logout()