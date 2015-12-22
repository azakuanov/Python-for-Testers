# -*- coding: utf-8 -*-
import unittest

from fixture.application import Application
from model.contact import Contact
import pytest


@pytest.fixture
def app (request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username ="admin", password = "secret")
    app.contact.add_contact(Contact(firstname = "Ferst", middlename="middle", lastname ="last", nickname ="Nick",
                             title = "Qa engineer", company = "startpack", address = "random addres"))
    app.session.logout()

