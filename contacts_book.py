from contact import Contact, db

class ContactsBook():

    def get_contacts(self):
        return Contact.query.all()

    def get_number_of_contacts(self):
        return len(Contact.query.all())

    def add_contact(self, username):
        contact = Contact(username)
        db.session.add(contact)
        db.session.commit()
