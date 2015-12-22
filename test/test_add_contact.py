
from model.contact import Contact



def test_test_add_contact(app):
    app.session.login(username ="admin", password = "secret")
    app.contact.add_contact(Contact(firstname = "Ferst", middlename="middle", lastname ="last", nickname ="Nick",
                             title = "Qa engineer", company = "startpack", address = "random addres"))
    app.session.logout()

