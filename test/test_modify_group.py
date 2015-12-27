from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="firstgroup", header = "jj"))
    app.group.modify_first_group(Group(name ="ModifiedName"))



def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="firstgroup", header = "jj"))
    app.group.modify_first_group(Group(header ="ModifiedHeader"))
