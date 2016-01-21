
from model.contact import Contact
import pytest
from data.contacts import testdata
import random
import string



def test_test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    if check_ui:
        #assert new_groups == app.group.get_group_list
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_group_list(), key = Contact.id_or_max)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

