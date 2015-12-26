
from model.contact import Contact



def test_test_add_contact(app):
    app.contact.add_contact(Contact(firstname = "Privet777" , middlename="middle", lastname ="last", nickname ="Nick",
                             title = "Qa engineer", company = "startpack", address = "random addres"))

