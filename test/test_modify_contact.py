import time
from model.contact import Contact



def test_test_add_contact(app):
    app.contact.delete_all_contacts()
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="firstgroup", middlename = "jj"))
    app.contact.modify_contact(Contact(firstname = "ModifyFerst", middlename="Modifymiddle", lastname ="Modifylast", nickname ="ModifyNick",
                             title = "ModifyQa engineer", company = "Modifystartpack", address = "Modifyrandom addres"))





