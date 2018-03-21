# importing all necessary functions/modules
from addressbook.supporting_func import check_if_contact_exists2
from addressbook.supporting_func import printing_format2
import csv

# downloading latest address book from csv file
addressbook_filename = "address_book.csv"
addressbook = []
try:
    with open(addressbook_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            addressbook.append(row)
except FileNotFoundError as fnf_error:
    print(f'There is no such file in directory: {fnf_error.filename}')
    print('Make sure you copied the file into correct folder!')


# defining class for Contacts
class Contact:
    # contact_count = 0

    def __init__(self, keycon, name, surname, adres, telno):
        self.contact_key = keycon
        self.first_name = name
        self.last_name = surname
        self.address = adres
        self.mobile_phone = telno
        # Contact.contact_count += 1

    # def __del__(self):
    #     Contact.contact_count += -1

    def rm_from_class(self,  name, surname, adres, telno):
        p = Contact(self,  name, surname, adres, telno)
        del p
        # Contact.contact_count += -1


# counting number of contacts and creating list of available record ids
# assigning contacts information downloaded from csv to class objects
# this is additional information needed to perform respective functions
addressbook_counter = 0
contact_ids = []
contact_list = []
for m in range(1, len(addressbook)):
    c = Contact(addressbook[m][0],
                addressbook[m][1],
                addressbook[m][2],
                addressbook[m][3],
                addressbook[m][4])
    contact_list.append(c)
    contact_ids.append(contact_list[addressbook_counter].contact_key)
    addressbook_counter += 1


# printing out for the user current state of address book
print()
print('This is how the address book currently looks like:\n')
print('record id | first name | last name | address | mobile phone')
for i in range(0, addressbook_counter):
    printing_format2(contact_list, i)
print()

# until action is equal 1/2/3/4 we will be asking user for all of his actions
# action 5 will break the loop
loop_repeat = True
text = 'Please provide action number (1 - add to address book, ' \
       '2 - remove from address book, ' \
       '3 - verify if exists, 4 - get number of contacts in address book, ' \
       '5 - end the program): '

while loop_repeat:

    # requesting action number from user
    action = int(input(text))

    # validating user input
    while action != 1 and action != 2 and action != 3 and action != 4 \
            and action != 5:
        print('You entered wrong data. '
              'Please provide whole umber between 1 and 5')
        action = int(input(text))

    # performing actions
    if action == 1:
        # we ask to provide new contact details
        first_name = input("Provide first name: ")
        last_name = input("Provide last name: ")
        address = input("Provide address: ")
        tel = input("Provide mobile phone number: ")
        # we will add new class object,
        # change address book counter and ids/contact list
        # only in case the record was added
        # so doesn't exist already in address book
        if check_if_contact_exists2(contact_list, first_name.title(), last_name.title(), addressbook_counter)[0] == 'No':
            new_id = int(max(contact_ids))
            new_id = new_id + 1
            c_new = Contact(new_id, first_name.title(),
                            last_name.title(), address, tel)
            contact_list.append(c_new)
            addressbook_counter += 1
            print('The contact has already been added to address book as per below:')
            printing_format2(contact_list, addressbook_counter - 1)
            print()
        else:
            print('The contact already exists in address book as per below:')
            id = check_if_contact_exists2(contact_list, first_name, last_name,
                                          addressbook_counter)[1]
            printing_format2(contact_list, id)
            print()


    elif action == 2:
        # we ask to provide contact name and surname details for removal
        first_name = input("Provide first name: ")
        last_name = input("Provide last name: ")
        # we will remove class object,
        # change address book counter and ids/contact list
        # only in case the record was deleted
        # so it exists already in address book
        if check_if_contact_exists2(contact_list, first_name,
                                                      last_name,
                                                      addressbook_counter)[0] == 'Yes':
            print('The following contact will be removed:')
            id = check_if_contact_exists2(contact_list, first_name, last_name,
                                          addressbook_counter)[1]
            printing_format2(contact_list, id)
            Contact.rm_from_class(id,
                                     contact_list[id].first_name,
                                     contact_list[id].last_name,
                                     contact_list[id].address,
                                     contact_list[id].mobile_phone)
            addressbook_counter += -1
            del contact_list[id]
            del contact_ids[id]
            print()
        else:
            print('There is no such contact for deletion!')
            print()


    elif action == 3:
        # we ask to provide contact name and surname details for verification
        first_name = input("Provide first name: ")
        last_name = input("Provide last name: ")
        if check_if_contact_exists2(contact_list, first_name, last_name, addressbook_counter)[0] == 'Yes':
            print('The contact already exists in address book as per below:')
            id = check_if_contact_exists2(contact_list, first_name, last_name, addressbook_counter)[1]
            printing_format2(contact_list, id)
            print()
        else:
            print('There is no such contact in address book')
            print()

    elif action == 4:
        # we provide number of contacts
        print(f'Currently there is {addressbook_counter} '
              f'contacts in address book')
        print('\n')

    else:
        # user is finishing his actions
        print('We will close and save the address book')
        loop_repeat = False

print(contact_ids)
# listing whole address book after changes
print('\n')
print('This is how the address book looks like after the changes:\n')
print('record id | first name | last name | address | mobile phone')
for j in range(0, addressbook_counter):
    printing_format2(contact_list, j)
print()



# saving the file to csv
with open(addressbook_filename, 'w') as f:
    f.write('record id;first name;last name;address;mobile phone\n')
    for k in range(0, addressbook_counter):
        line = str(contact_list[k].contact_key) + ';' + \
               str(contact_list[k].first_name) + ';' + \
               str(contact_list[k].last_name) + ';' + \
               str(contact_list[k].address) + ';' + \
               str(contact_list[k].mobile_phone) + '\n'
        f.write(line)


print('Address book saved in csv format!')


