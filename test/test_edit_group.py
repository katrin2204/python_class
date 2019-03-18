from model.group import Group


def test_edit_group_name(app):
    app.group.edit(Group(name="New Group Name"))


def test_edit_group_header(app):
    app.group.edit(Group(header="New Group Header"))


def test_edit_group_footer(app):
    app.group.edit(Group(footer="New Group Footer"))
