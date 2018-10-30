from contact import Contact

class ContactsBook():

    def get_contacts(self):
        return Contact.query.all()

    def get_number_of_contacts(self):
        return len(Contact.query.all())
