import mysql.connector
from fixture.db import DbFixture


db = DbFixture(host="127.0.0.1", name = "addressbook", user = "root", password="")

try:
    l = db.get_contact_list()
    for intem in l:
        print (intem)
    print (len(l))
finally:
    pass #db.destroy()
