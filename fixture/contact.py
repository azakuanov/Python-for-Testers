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

    def delete_first_contact(self,index):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//td/input")[index].click()

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
        self.contact_cache = None

    def modify_first_contact (self, index, contact):
        self.modify_contact_by_index(index)

    def modify_contact_by_index (self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # open edit contact page
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def count (self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_xpath("//td/input"))


    def delete_all_contacts(self):
        wd = self.app.wd
        while self.count() != 0:
            self.delete_first_contact()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"): #//tr/td/
                cells = element.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname  = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                print(all_phones)
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone = all_phones[0], mobilephone = all_phones[1],
                                                  workphone = all_phones[2], secondaryphone = all_phones[2]))
        return list(self.contact_cache)

    def get_contact_to_edit_by_index (self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name ('entry') [index]
        cell = row.find_elements_by_tag_name ("td") [7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_view_by_index (self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name ('entry') [index]
        cell = row.find_elements_by_tag_name ("td") [6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page (self, index):
        wd = self.app.wd
        self.get_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname = firstname, lastname = lastname, id = id,
                       homephone = homephone, workphone = workphone,
                       mobilephone = mobilephone, secondaryphone = secondaryphone)