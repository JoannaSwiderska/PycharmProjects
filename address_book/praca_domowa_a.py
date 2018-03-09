# importing all necessary functions/modules
from addressbook.verify_contact import contact_vs_addressbook
from addressbook.add_contact import add_contact_to_addressbook
from addressbook.remove_contact import rm_contact_from_addressbook
import pickle

# downloading latest version of address book and assigning to variable
addressbook_filename = "address_book.pkl"
try:
    with open(addressbook_filename, "rb+") as addressbook_file:
        addressbook = pickle.load(addressbook_file)
except FileNotFoundError as fnf_error:
    print(f'There is no such file in directory: {fnf_error.filename}')
    print('Make sure you copied the file into correct folder!')
finally:
    addressbook_file.close()


# counting number of contacts and creating list of available record ids
# this is additional information needed to perform respective functions
addressbook_counter = 0
contact_ids = []
for key, element in addressbook.items():
    addressbook_counter += 1
    contact_ids.append(int(key))


# printing out for the user current state of address book
print('\n')
print('This is how the address book currently looks like:\n')
print('record id | first name | last name | address | mobile phone')
for i in range(0, addressbook_counter):
    print(f'{contact_ids[i]}', '|', addressbook[f'{contact_ids[i]}']['first name'], '|', addressbook[f'{contact_ids[i]}']['last name'],
          '|', addressbook[f'{contact_ids[i]}']['address'], '|', addressbook[f'{contact_ids[i]}']['mobile phone'])
print('\n')


# until action is equal 1/2/3/4 we will be asking user for all of his actions
# action 5 will break the loop
loop_repeat = True

while loop_repeat:

    # requesting action number from user
    action = int(
        input('Please provide action number (1 - add to address book, '
              '2 - remove from address book, 3 - verify if exists, '
              '4 - get number of contacts in address book, '
              '5 - end the program): '))

    # validating user input
    while action != 1 and action != 2 and action != 3 and action != 4 \
            and action != 5:
        print('You entered wrong data. '
              'Please provide whole umber between 1 and 5')
        action = int(
            input(
                'Please provide action number (1 - add to address book, '
                '2 - remove from address book, 3 - verify if exists, '
                '4 - get number of contacts in address book, '
                '5 - end the program): '))

    # performing actions
    if action == 1:
        # we ask to provide new contact details
        first_name = input("Provide first name: ")
        last_name = input("Provide last name: ")
        address = input ("Provide address: ")
        tel = input("Provide mobile phone number: ")
        addition_result = add_contact_to_addressbook(addressbook,
                                                     first_name.title(),
                                                     last_name.title(), address,
                                                     tel, addressbook_counter,
                                                     contact_ids)
        # we will change address book counter and ids list
        # only in case the record was added so the result in not equal 0
        if addition_result != 0:
            addressbook_counter += 1
            contact_ids.append(addition_result)

    elif action == 2:
        # we ask to provide contact name and surname details for removal
        first_name = input("Provide first name: ")
        last_name = input("Provide last name: ")
        removal_result = rm_contact_from_addressbook(addressbook, first_name,
                                                     last_name, addressbook_counter, contact_ids)
        # we will change address book counter and ids list
        # only in case the record was deleted so the result in not equal 0
        if removal_result != 0:
            addressbook_counter += (-1)
            contact_ids.remove(removal_result)

    elif action == 3:
        # we ask to provide contact name and surname details for verification
        first_name = input("Provide first name: ")
        last_name = input("Provide last name: ")
        contact_vs_addressbook(addressbook, first_name, last_name,
                               addressbook_counter, contact_ids)

    elif action == 4:
        print(f'Currently there is {addressbook_counter} '
              f'contacts in address book')
        print('\n')

    else:
        # user is finishing his actions
        print('We will close and save the address book')
        loop_repeat = False


# listing whole address book after changes
print('\n')
print('This is how the address book looks like after the changes:\n')
print('record id | first name | last name | address | mobile phone')
for j in range(0, addressbook_counter):
    print(f'{contact_ids[j]}', '|',
          addressbook[f'{contact_ids[j]}']['first name'],
          '|', addressbook[f'{contact_ids[j]}']['last name'],
          '|', addressbook[f'{contact_ids[j]}']['address'], '|',
          addressbook[f'{contact_ids[j]}']['mobile phone'])
print('\n')

# saving (overwriting) the newest version of address book
with open(addressbook_filename, "wb") as file:
    pickle.dump(addressbook, file)
file.close()


# saving the file also to csv so that the user can open it in excel for example
with open('address_book.csv', 'w') as f:
    f.write('record id ; first name ; last name ; address ; mobile phone\n')
    for k in range(0, addressbook_counter):
        line = f'{contact_ids[k]}' + ';' + \
               addressbook[f'{contact_ids[k]}']['first name'] + ';' \
               + addressbook[f'{contact_ids[k]}']['last name'] + ';' + \
               addressbook[f'{contact_ids[k]}']['address'] + ';' + \
               addressbook[f'{contact_ids[k]}']['mobile phone'] + '\n'
        f.write(line)


print('Address book saved in two formats!')


