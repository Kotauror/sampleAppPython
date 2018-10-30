from contact import Contact

class ContactsBook():

    def get_contacts(self):
        return Contact.query.all()
