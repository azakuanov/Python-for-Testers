from model.contact import Contact
from random import randrange



def test_modify_contact(app,  db, check_ui):
    old_contacts = db.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="firstgroup", middlename = "jj"))
    index = randrange (len(old_contacts))
    contact = Contact(firstname = "ModifyFerst", middlename="Modifymiddle", lastname ="Modifylast", nickname ="ModifyNick",
                             title = "ModifyQa engineer", company = "Modifystartpack", address = "Modifyrandom addres")

    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    print(sorted(old_contacts, key=Contact.id_or_max))
    print(sorted(new_contacts, key=Contact.id_or_max))
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        #assert new_groups == app.group.get_group_list
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.group.get_group_list(), key = Contact.id_or_max)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


