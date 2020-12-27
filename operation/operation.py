import threading
from threading import *
import time


keys = dict()  # 'keys' is the dictionary in which we store data


def create(key, value, timeout=0):
    '''
    For create operation
    use function create(key_name, value, timeout_value)
    Here, the timeout value is optional to use
    '''
    try:
        if key in keys:
            print("Error: The Key already exists")  # error message

        else:

            if(key.isalpha()):

                # constraints for file size less than 1.0GB and JSON object value less than 16KB
                if (
                    (len(keys) < (1024 * 1020 *
                                  1024)) and (value <= (16 * 1024 * 1024))
                ):

                    if timeout == 0:
                        c = [value, timeout]

                    else:
                        c = [value, timeout + time.time()]

                    if (len(key) <= 32):  # constraints for input key_name capped at 32chars
                        keys[key] = c

                else:
                    print("Error: Memory Limit Exceeded! ")  # error message

            else:
                # error message
                print("Error: Invalind key_name!! Key must contain only alphabets!")

    except Exception as e:
        print(e)


def read(key):
    '''
    For read operation of the key
    use function "read(key_name)" to read any key
    '''
    try:

        if key not in keys:
            # error message
            print("Error: Given Key does'nt exists. Please enter a valid key")

        else:

            data = keys[key]

            if data[1] == 0:
                data = str(key) + ":" + str(data[0])
                return data

            else:
                # comparing the present time w.r.t expiry time
                if time.time() < data[1]:

                    # to return the value in the format of JSON Object in the form of "key_name: value"
                    data = str(key) + ":" + str(data[0])
                    return data

                else:
                    print("Error: Time-To-Live of '", key,
                          "' has been Expired")  # error message

    except Exception as e:
        print(e)


def delete(key):
    '''
    For delete operation of the key value
    use function "delete(key_name)" to delete any key
    '''
    try:

        if key not in keys:
            # error message
            print("Error: Key does not exists. Please enter a valid key")

        else:

            oper = keys[key]

            if oper[1] != 0:

                # comparing the current time w.r.t expiry time
                if time.time() < oper[1]:
                    del keys[key]
                    print("Key Deleted Successfully!!")

                else:
                    print("Error: Time-To-Live of '", key,
                          "' has been expired")  # error message

            else:
                del keys[key]
                print("Key is successfully deleted!!")

    except Exception as e:
        print(e)


def modify(key, value):
    '''
    For modify operation (modifying the key)
    use function "modify(key_name, new_value)"
    '''
    try:

        oper = keys[key]  # taking out the key from keys

        if oper[1] == 0:

            if key not in keys:
                # error message
                print("Error: Key does'nt exists. Please enter a valid key")

            else:
                values = []
                values.append(value)
                values.append(oper[1])
                keys[key] = values

        else:
            if time.time() < oper[1]:

                if key not in keys:
                    # error message
                    print(
                        "Error: Key does'nt exists. Please enter a valid key")

                else:
                    values = []
                    values.append(value)
                    values.append(oper[1])
                    keys[key] = values

            else:
                print("Error: Time-To-Live of '", key,
                      "' has been expired")  # error message

    except Exception as e:
        print(e)
