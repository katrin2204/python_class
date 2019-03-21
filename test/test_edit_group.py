from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit(Group(name="New Group Name"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit(Group(header="New Group Header"))


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit(Group(footer="New Group Footer"))
