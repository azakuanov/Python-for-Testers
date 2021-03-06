from sys import maxsize

class Contact:

    def __init__(self ,firstname = None, middlename = None, lastname = None, nickname = None, title = None, company = None, address = None,
                 id = None, homephone = None, workphone = None, mobilephone = None, secondaryphone = None, all_phones_from_home_page = None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.id = id
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.firstname, self.lastname, self.address, self.homephone, self.workphone, self.mobilephone, self.secondaryphone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if  self.id:
            return int(self.id)
        else:
            return maxsize
