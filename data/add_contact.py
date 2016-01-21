from model.contact import Contact
import random
import string


def random_string (prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range( random.randrange(maxlen))])


test_data = [Contact(firstname = "", middlename = "", lastname = "")] + [

        Contact(firstname = random_string("firstname", 10), middlename = random_string("middlename", 20), lastname = random_string("lastname", 20))
        for i in range(5)
    ]
