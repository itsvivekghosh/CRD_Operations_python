import operation.code as op


# creating key_value having no time-out-value
op.create("first", 60)

# creating key_value having time-out-value
op.create("second", 100, 120)

# reading key_value
op.read('first')
op.read("second")


# delete the key_value
op.delete("first")
op.delete("second")


# this line will generate error as 'third' key-value is in the database
op.delete("third")
