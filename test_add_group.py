# -*- coding: utf-8 -*-

from application import Application
import unittest
import pytest
from group import Group


@pytest.fixture
def app (request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_python(app):
    app.login( login = "admin", password = "secret")
    app.create_new_group(Group(name = "RandomName", header = "RandomHeader", footer = "RandomFooter"))
    app.logout()
