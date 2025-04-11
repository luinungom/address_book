from Contact import Contact
from ContactsService import ContactsService


class AddressBook:

    def __init__(self):
        self.contacts = []
        self.contactsService = ContactsService()

    def address_book(self):
        operation_ended: bool = False
        print('*** Welcome to the Address Book ***')
        for contact in self.contactsService.get_contacts():
            print(contact)
        while not operation_ended:
            try:
                operation: int = self.show_menu()
                operation_ended = self.execute_operation(operation)
            except ValueError as e:
                print(f'Invalid value: {e}')

    def show_menu(self):
        print(f'Operations:')
        print('1. Add Contact')
        print('2. Find Contact')
        print('3. Delete Contact')
        print('4. Show all contacts')
        print('5. Exit')
        return int(input('Select an option: '))

    def execute_operation(self, operation: int):
        if operation == 1:
            self.add_contact()
        elif operation == 2:
            self.find_contact()
        elif operation == 3:
            self.delete_contact()
        elif operation == 4:
            self.show_contacts()
        elif operation == 5:
            return True
        else:
            print('Invalid option')
        return False

    def add_contact(self):
        try:
            name = input('Name: ')
            if len(name) == 0:
                raise ValueError('Name cannot be empty')
            phone = input('Phone: ')
            if len(phone) == 0:
                raise ValueError('Phone cannot be empty')
            email = input('Email: ')
            if not '@' in email or not '.' in email:
                raise ValueError('Invalid email')
            contact = Contact(name, phone, email)
            self.contactsService.add_contact(contact)
            print('Contact added successfully')
        except ValueError as e:
            print(f'Invalid value: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def find_contact(self):
        try:
            name = input('Name: ')
            contact = self.contactsService.get_contact(name)
            if contact is None:
                print('Contact not found')
            else:
                print(contact)
        except ValueError as e:
            print(f'Invalid value: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def delete_contact(self):
        try:
            name = input('Name: ')
            contact = self.contactsService.get_contact(name)
            if contact is None:
                print('Contact not found')
            else:
                self.contactsService.remove_contact(contact)
                print('Contact deleted successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def show_contacts(self):
        for contact in self.contactsService.get_contacts():
            print(contact)

if __name__ == '__main__':
    address_book = AddressBook()
    address_book.address_book()
