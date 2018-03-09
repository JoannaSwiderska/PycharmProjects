def check_if_contact_exists(database, name, surname, database_counter,
                            database_ids):
    """
    this is supporting function
    we check if contact name and surname exists in database

    :return: YES/No if the contact exists in address book
    and record id if YES or 0 in case of NO
    """

    exists = False
    found_i = 0

    for i in range(0, database_counter):
        if database[f'{database_ids[i]}']['first name'].upper() == \
                name.upper() \
                and database[f'{database_ids[i]}']['last name'].upper() == \
                surname.upper():
            found_i = i
            exists = True
        else:
            continue

    if exists:
        return ['Yes', database_ids[found_i]]
    else:
        return ['No', 0]


def contact_vs_addressbook(database, name, surname, database_counter,
                           database_ids):
    """
    once the contact is validated
    function returns appropriate information

    :return: information message for user whether contact exists in database
    """

    if check_if_contact_exists(database, name, surname, database_counter,
                               database_ids)[0] == 'Yes':
        print('The contact already exists in address book as per below:')
        id = check_if_contact_exists(database, name, surname, database_counter,
                                     database_ids)[1]
        print(str(id), '|', database[f'{id}']['first name'], '|',
              database[f'{id}']['last name'],
              '|', database[f'{id}']['address'], '|',
              database[f'{id}']['mobile phone'])
        print('\n')
    else:
        print('There is no such contact in address book')
        print('\n')