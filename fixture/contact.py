import time
class ContactHelper:

    def __init__(self, app):

        self.app = app



    def open_home_page (self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//td/input").click()


    def go_to_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

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


    def modify_contact (self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open edit contact page
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()

    def count (self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_xpath("//td/input"))


    def delete_all_contacts(self):
        wd = self.app.wd
        while self.count() != 0:
            self.delete_first_contact()