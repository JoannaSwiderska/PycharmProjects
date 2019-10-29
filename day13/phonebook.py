class Contact:
    contacts_no = 0
    last_id = 0

    def __init__(self, name, lastname):
        Contact.last_id += 1
        self.id = Contact.last_id
        self.name = name
        self.lastname = lastname
        Contact.contacts_no += 1

    def full_name(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return f'ID: {self.id} Name: {self.name} Lastname: {self.lastname}'

    def __repr__(self):
        return f'Contact({self.name}, {self.lastname})'

    def __del__(self):
        print('called', self.id)
        Contact.contacts_no -= 1


class Phonebook:
    def __init__(self):
        self.__data = dict()

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        elements = [f'{k} -> {v}' for k, v in self.__data.items()]
        elements_with_new_lines = '\n'.join(elements)
        return elements_with_new_lines

    def __iter__(self):
        pass

    def __getitem__(self, item):
        return self.__data[item]

    def __delitem__(self, key):
        return self.__data.pop(key)

    def __repr__(self):
        return self.__str__()

    def add_contact(self, contact):
        self.__data[contact.id] = contact

    def remove_contact(self, contact):
        self.__delitem__(contact.id)



if __name__ == '__main__':
    from pprint import pprint


    c = Contact('Jan', 'Kowalski')
    c2 = Contact('Adam', 'Nowak')
    print(c)
    print(c2)
    contacts = [c, c2, Contact('Pawel', 'Nowak')]
    pprint(contacts)
    del contacts[1]
    del contacts[1]
    pprint(contacts)
    print(Contact.contacts_no)

    phonebook = Phonebook()
    phonebook.add_contact(c)
    phonebook.add_contact(c2)
    phonebook.add_contact(Contact('Pawel', 'Nowak'))
    # print(phonebook)
    # print(phonebook[1])
    # print(phonebook[2])
    # print('*'*80)
    phonebook.remove_contact(c)

    # for contact in phonebook:
    #     print(contact)