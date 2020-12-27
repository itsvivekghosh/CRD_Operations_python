import threading
from threading import *
import time


keys = dict()  # 'keys' is the dictionary in which we store data


try:
    def create(key, value, timeout=0):
        '''
        For create operation
        use function create(key_name, value, timeout_value)
        Here, the timeout value is optional to use
        '''
        if key in keys:
            print("Error: The Key already exists")  # error message1

        else:

            if(key.isalpha()):

                # constraints for file size less than 1.0GB and JSON object value less than 16KB
                if len(keys) < (1024*1020*1024) and value <= (16*1024*1024):

                    if timeout == 0:
                        c = [value, timeout]

                    else:
                        c = [value, timeout + time.time()]

                    if len(key) <= 32:  # constraints for input key_name capped at 32chars
                        keys[key] = c

                else:
                    print("Error: Memory Limit Exceeded! ")  # error message2

            else:
                # error message3
                print("Error: Invalind key_name!! Key must contain only alphabets!")
except Exception as e:
    print(e)


def read(key):
    ''' 
    For read operation of the key
    use function "read(key_name)" to read any key
    '''
    if key not in keys:
        # error message4
        print("Error: Given Key does'nt exists. Please enter a valid key")
    else:
        data = keys[key]
        if data[1] != 0:
            if time.time() < data[1]:  # comparing the present time with expiry time
                # to return the value in the format of JSON Object i.e.,"key_name: value"
                stri = str(key)+":"+str(data[0])
                return stri
            else:
                print("Error: Time-To-Live of '", key,
                      "' has been Expired")  # error message5
        else:
            stri = str(key)+":"+str(data[0])
            return stri


def delete(key):
    ''' 
    For delete operation of the key value
    use function "delete(key_name)" to delete any key
    '''
    if key not in keys:
        # error message4
        print("Error: Key does not exists. Please enter a valid key")
    else:
        oper = keys[key]
        if oper[1] != 0:
            if time.time() < oper[1]:  # comparing the current time with expiry time
                del keys[key]
                print("Key Deleted Successfully!!")
            else:
                print("Error: Time-To-Live of '", key,
                      "' has been expired")  # error message5
        else:
            del keys[key]
            print("Key is successfully deleted!!")


def modify(key, value):
    '''
    For modify operation (modifying the key)
    use function "modify(key_name, new_value)"
    '''
    oper = keys[key]
    if oper[1] != 0:
        if time.time() < oper[1]:
            if key not in keys:
                # error message6
                print(
                    "Error: Key does'nt exists. Please enter a valid key")
            else:
                values = []
                values.append(value)
                values.append(oper[1])
                keys[key] = values
        else:
            print("Error: Time-To-Live of '", key,
                  "' has been expired")  # error message5
    else:
        if key not in keys:
            # error message6
            print("Error: Key does'nt exists. Please enter a valid key")
        else:
            values = []
            values.append(value)
            values.append(oper[1])
            keys[key] = values
