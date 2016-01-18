from model.group import Group


def test_add_group(app, db, json_test, check_ui):
    group = json_test
    old_groups = db.get_group_list()
    app.group.create_new_group(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        #assert new_groups == app.group.get_group_list
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)


#def test_add_empty_group(app):
 #   old_groups = app.group.get_group_list()
  #  group = Group(name = "", header = "", footer = "")
   # app.group.create_new_group(group)
    #new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
 #   old_groups.append(group)
  #  assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



