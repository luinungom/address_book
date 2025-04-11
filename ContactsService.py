import os.path

from Contact import Contact


class ContactsService:
    FILE_NAME = "contacts.txt"

    def __init__(self):
        self.contacts_list = []
        if os.path.exists(self.FILE_NAME):
            self.contacts_list = self.load_contacts_from_file()
        else:
            self.contacts_list = self.load_initial_contacts()

    def load_initial_contacts(self):
        initial_contacts = [
            Contact("Valentino Rossi", "646464646", "thedoctor@rossi.com"),
            Contact("Michael Doohan", "611111111", "doohan@ok.com"),
        ]
        self.save_contacts_in_file(initial_contacts)
        return initial_contacts

    def save_contacts_in_file(self, contacts):
        try:
            with open(self.FILE_NAME, "w") as file:
                for contact in contacts:
                    file.write(contact.write_contact() + "\n")
        except Exception as e:
            print(f"Error saving contacts in file: {e}")

    def load_contacts_from_file(self):
        contacts = []
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    name, phone, email = line.strip().split(",")
                    contact = Contact(name, phone, email)
                    contacts.append(contact)
                return contacts
        except Exception as e:
            print(f"Error loading contacts from file: {e}")

    def add_contact(self, contact):
        self.contacts_list.append(contact)
        self.save_contacts_in_file(self.contacts_list)

    def remove_contact(self, contact):
        self.contacts_list.remove(contact)
        self.save_contacts_in_file(self.contacts_list)

    def get_contact(self, name: str):
        for contact in self.contacts_list:
            if contact.name == name:
                return contact

    def get_contacts(self):
        return self.contacts_list
