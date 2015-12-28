from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="firstgroup", header = "jj"))
    group = Group(name ="ModifiedName")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="firstgroup", header = "jj"))
    app.group.modify_first_group(Group(header ="ModifiedHeader"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
