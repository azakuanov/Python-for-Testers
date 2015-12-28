import time
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):

        self.app = app



    def open_home_page (self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_link_text("home page")) > 0):
            wd.find_element_by_link_text("home page").click()

    def go_to_create_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//td/input").click()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_contact(self, contact):
        wd = self.app.wd
        self.go_to_create_contact_page()
        self.fill_contact_fields(contact)
        # click submit button
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()


    def modify_contact (self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open edit contact page
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def count (self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_xpath("//td/input"))


    def delete_all_contacts(self):
        wd = self.app.wd
        while self.count() != 0:
            self.delete_first_contact()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"): #//tr/td/
            cells = element.find_elements_by_tag_name('td')
            firstname = cells[2].text
            lastname  = cells[1].text
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts