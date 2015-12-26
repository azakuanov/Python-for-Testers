from model.group import Group
import time


def test_del_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="firstgroup", header = "jj"))
    app.group.delete_first_group()

