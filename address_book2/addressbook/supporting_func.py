def check_if_contact_exists2(database, name, surname, database_counter):
    """
    this is supporting function
    we check if contact name and surname exists in database

    :return: YES/No if the contact exists in address book
    and record id if YES or 0 in case of NO
    """

    exists = False
    found_i = 0

    for i in range(0, database_counter):
        if database[i].first_name.upper() == \
                name.upper() \
                and database[i].last_name.upper() == \
                surname.upper():
            found_i = i
            exists = True
        else:
            continue

    if exists:
        return ['Yes', found_i]
    else:
        return ['No', 0]




def printing_format2(database, x):
    """
    this is supporting function
    that prepares contact details for printing

    :return: formatted contact
    """

    print(database[x].contact_key, '|',
          database[x].first_name, '|',
          database[x].last_name, '|',
          database[x].address, '|',
          database[x].mobile_phone)


# def contact_vs_addressbook2(database, name, surname, database_counter):
#     """
#     once the contact is validated
#     function returns appropriate information
#
#     :return: information message for user whether contact exists in database
#     """
#
#     if check_if_contact_exists2(database, name, surname, database_counter)[0] == 'Yes':
#         print('The contact already exists in address book as per below:')
#         id = check_if_contact_exists2(database, name, surname, database_counter)[1]
#         printing_format2(database, id)
#         print()
#     else:
#         print('There is no such contact in address book')
#         print()



# def add_contact_to_addressbook2(database, name, surname, address, tel_no,
#                                database_counter, database_ids, Class):
#     """
#     we check if contact name and surname exists in database
#     using imported function
#     if no we add new contact details
#
#     :return: new record id or 0 in case the contact already exists so there is
#     no point for adding
#     """
#
#     if check_if_contact_exists2(database, name, surname, database_counter)[0] == 'No':
#         new_id = int(max(database_ids))
#         new_id = new_id + 1
#         c_new = Class(new_id, name.title(),
#                       surname.title(), address, tel_no)
#         database.append(c_new)
#         print('The contact has already been added to address book as per below:')
#         printing_format2(database, database_counter + 1)
#         print()
#         return str(new_id)
#     else:
#         print('The contact already exists in address book as per below:')
#         id = check_if_contact_exists2(database, name, surname, database_counter)[1]
#         printing_format2(database, id)
#         print()
#         return 0


# def rm_contact_from_addressbook2(database, name, surname, database_counter,
#                                 database_ids):
#     """
#     we check if contact name and surname exists in database
#     using imported function
#     if yes we remove it
#
#     :return: removed record id or 0 in case the contact doesn't exist
#     so we cannot remove
#     """
#
#     if check_if_contact_exists2(database, name, surname, database_counter,
#                                database_ids)[0] == 'Yes':
#         print('The following contact will be removed:')
#         id = check_if_contact_exists2(database, name, surname, database_counter,
#                                      database_ids)[1]
#         printing_format2(database, id)
#         # print(database[id].contact_count)
#         # del database[id]
#         # print(database[id-1].contact_count)
#         # print(Contact.contact_count)
#         print()
#         return str(id)
#     else:
#         print('There is no such contact for deletion!')
#         print()
#         return 0



