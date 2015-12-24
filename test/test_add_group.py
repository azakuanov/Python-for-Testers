from model.group import Group
import time


def test_add_group(app):
    app.group.create_new_group(Group(name = "RandomName", header = "RandomHeader", footer = "RandomFooter"))
   # time.sleep(5)


def test_add_empty_group(app):
    app.group.create_new_group(Group(name = "", header = "", footer = ""))


