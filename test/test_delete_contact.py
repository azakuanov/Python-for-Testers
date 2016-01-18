from model.contact import Contact
from random import randrange


def test_del_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="firstgroup", middlename = "jj"))
    old_contacts = db.get_contact_list()
    index = randrange (len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    #old_contacts[index:index +1] = []
    assert old_contacts == new_contacts
    if check_ui:
        #assert new_groups == app.group.get_group_list
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)