from contact import Contact

class ContactsBook():

    def get_contacts(self):
        return Contact.query.all()

    def get_number_of_contacts(self):
        return len(Contact.query.all())

    def get_contacts_names_as_string(self):
        contacts = Contact.query.all()
        str_list = []
        for contact in contacts:
            str_list.append(contact.name)
        return ', '.join(str_list)
