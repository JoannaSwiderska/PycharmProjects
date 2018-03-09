def add_contact_to_addressbook(database, name, surname, address, tel_no,
                               database_counter, database_ids):
    """
    we check if contact name and surname exists in database
    using imported function
    if no we add new contact details

    :return: new record id or 0 in case the contact already exists so there is
    no point for adding
    """

    from addressbook.verify_contact import check_if_contact_exists

    if check_if_contact_exists(database, name, surname, database_counter,
                               database_ids)[0] == 'No':
        new_id = max(database_ids) + 1
        database.update({str(new_id): {'first name': name, 'last name': surname,
                                       'address': address,
                                       'mobile phone': tel_no}})
        print('The contact has already been added to address book as per below:')
        print(str(new_id), '|', database[f'{new_id}']['first name'], '|',
              database[f'{new_id}']['last name'],
              '|', database[f'{new_id}']['address'], '|',
              database[f'{new_id}']['mobile phone'])
        print('\n')
        return new_id
    else:
        print('The contact already exists in address book as per below:')
        id = check_if_contact_exists(database, name, surname, database_counter,
                                     database_ids)[1]
        print(str(id), '|', database[f'{id}']['first name'], '|',
              database[f'{id}']['last name'],
              '|', database[f'{id}']['address'], '|',
              database[f'{id}']['mobile phone'])
        print('\n')
        return 0

