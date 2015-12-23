from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password ="secret")
    app.group.modify_group(Group(name = "ModifiedName", header = "ModifiedHeader", footer = "ModifiedFooter"))
    app.session.logout()