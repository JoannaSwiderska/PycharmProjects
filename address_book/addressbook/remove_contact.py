def rm_contact_from_addressbook(database, name, surname, database_counter,
                                database_ids):
    """
    we check if contact name and surname exists in database
    using imported function
    if yes we remove it

    :return: removed record id or 0 in case the contact doesn't exist
    so we cannot remove
    """

    from addressbook.verify_contact import check_if_contact_exists

    if check_if_contact_exists(database, name, surname, database_counter,
                               database_ids)[0] == 'Yes':
        print('The following contact will be removed:')
        id = check_if_contact_exists(database, name, surname, database_counter,
                                     database_ids)[1]
        print(str(id), '|', database[f'{id}']['first name'], '|',
              database[f'{id}']['last name'],
              '|', database[f'{id}']['address'], '|',
              database[f'{id}']['mobile phone'])
        del database[f'{id}']
        print('\n')
        return id
    else:
        print('There is no such contact for deletion!')
        print('\n')
        return 0
