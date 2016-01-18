
from model.contact import Contact
import pytest
import random
import string

def random_string (prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range( random.randrange(maxlen))])


test_data = [Contact(firstname = "", middlename = "", lastname = "")] + [

        Contact(firstname = random_string("firstname", 10), middlename = random_string("middlename", 20), lastname = random_string("lastname", 20))
        for i in range(5)
    ]

@pytest.mark.parametrize("contact", test_data, ids = [repr(x) for x in test_data])

def test_test_add_contact(app, contact, db, check_ui):
    old_contacts = db.get_contact_list()
    contact = Contact(firstname = "Privet777" , middlename="middle", lastname ="last", nickname ="Nick",
                             title = "Qa engineer", company = "startpack", address = "random addres")
    app.contact.add_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    if check_ui:
        #assert new_groups == app.group.get_group_list
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_group_list(), key = Contact.id_or_max)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

