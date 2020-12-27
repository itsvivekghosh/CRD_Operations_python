# CRD Operations using Python

Building a file-based key-value data store for basic CRD Operations ( Creating, Reading and Deleting Key Values).

### The data store will support the following :

1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32 characters. The value is always a JSON object - capped at 16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits

### Non functional requirements:

1. The file size never exceeds 1GB
2. The file is accessed by multi-threading

---

## Working

The main file are main.py and operation.py (inside operations directory) file. inorder to get through the working we can use the commands as:

We have to import the main file to access the operations. And, this can be imported by below line:<br>
`import operation.operation as op`

1. Creating a Key:
   `op.create(key_value, value, timeout)`

2. Reading a Key:
   `op.read(key_value)`

3. Deleting a Key:
   `op.delete(key_value)`

---

The substequent errors will be generated for the operations.
