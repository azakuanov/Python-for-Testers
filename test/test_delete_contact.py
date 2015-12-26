from model.contact import Contact



def test_del_contact(app):
    app.contact.delete_all_contacts()
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="firstgroup", middlename = "jj"))
    app.contact.delete_first_contact()
