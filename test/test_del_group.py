from model.group import Group
import time


def test_del_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="firstgroup", header = "jj"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
