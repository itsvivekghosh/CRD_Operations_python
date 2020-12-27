import operation.operation as op
import threading
from threading import *


def create():
    # creating key_value having no time-out-value
    op.create("first", 60)

    # creating key_value having time-out-value
    op.create("second", 100, 120)
    # the last parameter is time-out value that tells the time-out of the key-value
    # after the time-out-value the key-value will be destroyed or we can't use that.

    # creating an error key-value
    op.create('first#$%^&error_key', 80)
    op.create('first5error_key', 70)
    # these all lines will generate error as the key_value cannot contain special characters or numeric keywords.


def read():
    # reading key_value
    op.read('first')
    op.read("second")
    # after the time-out-value the 'second' value will generate error while reading


def delete():
    # delete the key_value
    op.delete("first")
    op.delete("second")
    # after the time-out-value the 'second' value will generate error while reading

    # this line will generate error as 'third' key-value is in the database
    op.delete("third")


if __name__ == '__main__':
    create()
    read()
    delete()
