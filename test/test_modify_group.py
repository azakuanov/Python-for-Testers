from model.group import Group
from random import randrange

from model.group import Group

def test_modify_group_name(app, db, check_ui):
    old_groups = db.get_group_list()
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="firstgroup", header = "jj"))
    index = randrange (len(old_groups))
    group = Group(name ="ModifiedName")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert new_groups == app.group.get_group_list
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)




def test_modify_group_header(app, db):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="firstgroup", header = "jj"))
    old_groups = db.get_group_list()
    index = randrange (len(old_groups))
    group =Group(header ="ModifiedHeader")
    app.group.modify_group_by_index(index, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
