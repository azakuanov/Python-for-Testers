
from model.contact import Contact



def test_test_add_contact(app):
    app.session.login(username ="admin", password = "secret")
    app.contact.modify_contact(Contact(firstname = "ModifyFerst", middlename="Modifymiddle", lastname ="Modifylast", nickname ="ModifyNick",
                             title = "ModifyQa engineer", company = "Modifystartpack", address = "Modifyrandom addres"))
    app.session.logout()

