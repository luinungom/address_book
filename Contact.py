class Contact:

    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'Name: {self.name}, Phone: {self.phone}, Email: {self.email}'

    def write_contact(self):
        return f'{self.name},{self.phone},{self.email}'
