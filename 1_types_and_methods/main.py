# Integer
my_int = 10
print("my_int = 10")
print("type(my_int): ", type(my_int))  # Output: <class 'int'>
print() # newline

# Float
my_float = 3.14
print("my_float = 3.14")
print("type(my_float): ", type(my_float))  # Output: <class 'float'>
print() # newline

# String
my_string = "Hello, World!"
print("my_string = 'Hello, World!'")
print("type(my_string): ", type(my_string))  # Output: <class 'str'>
# String methods
print("my_string.upper(): ", my_string.upper() )  # Output: "HELLO, WORLD!"
print("my_string.lower: ", my_string.lower())  # Output: "hello, world!"
print("my_string.capitalize(): ", my_string.capitalize())  # Output: "Hello, world!"
print('my_string.replace("Hello", "Hi"): ', my_string.replace("Hello", "Hi"))  # Output: "Hi, World!"
print("my_string.split(","): ", my_string.split(","))  # Output: ["Hello", " World!"]
print() # newline

# Boolean
my_bool = True
print("my_bool = True")
print("type(my_bool): ", type(my_bool))  # Output: <class 'bool'>
print() # newline

# List
my_list = [1, 2, 3, 4, 5]
print("my_list = [1, 2, 3, 4, 5]")
print("type(my_list): ", type(my_list))  # Output: <class 'list'>
# List methods
print("len(my_list): ", len(my_list))  # Output: 5
my_list.append(6)
print("my_list.append(6): ", my_list)  # Output: [1, 2, 3, 4, 5, 6]
my_list.pop()
print("my_list.pop(): ", my_list)  # Output: 6
my_list.reverse()
print("my_list.reverse(): ", my_list)  # Output: [5, 4, 3, 2, 1]
my_list.sort()
print("my_list.sort(): ", my_list)  # Output: [1, 2, 3, 4, 5]
print() # newline

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("my_tuple = (1, 2, 3, 4, 5)")
print("type(my_tuple): ", type(my_tuple))  # Output: <class 'tuple'>
# Tuple methods
print("len(my_tuple): ", len(my_tuple))  # Output: 5
print("my_tuple.count(3): ", my_tuple.count(3))  # Output: 1
print("my_tuple.index(4): ", my_tuple.index(4))  # Output: 3
print() # newline

# Set
my_set = {1, 2, 3, 4, 5}
print("my_set = {1, 2, 3, 4, 5}")
print("type(my_set): ", type(my_set))  # Output: <class 'set'>
# Set methods
print("len(my_set): ", len(my_set))  # Output: 5
my_set.add(6)
print("my_set.add(6): ", my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.remove(3)
print("my_set.remove(3): ", my_set)  # Output: {1, 2, 4, 5}
print("my_set.union({6, 7, 8}): ", my_set.union({6, 7, 8}))  # Output: {1, 2, 4, 5, 6, 7, 8}
print("my_set.intersection({4, 5, 6}): ", my_set.intersection({4, 5, 6}))  # Output: {4, 5}
print() # newline

# Dictionary
my_dict = {"name": "John", "age": 30}
print("my_dict = {'name': 'John', 'age': 30}")
print("type(my_dict): ", type(my_dict))  # Output: <class 'dict'>
# Dictionary methods
print("len(my_dict): ", len(my_dict))  # Output: 2
print("my_dict.keys(): ", my_dict.keys())  # Output: dict_keys(['name', 'age'])
print("my_dict.values(): ", my_dict.values())  # Output: dict_values(['John', 30])
print("my_dict.items(): ", my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30)])
print() # newline

# Range
my_range = range(5)
print("my_range = range(5)")
print("type(my_range): ", type(my_range))  # Output: <class 'range'>
# Range methods
print("len(my_range): ", len(my_range))  # Output: 5
print("list(my_range): ", list(my_range))  # Output: [0, 1, 2, 3, 4]
print("my_range.start: ", my_range.start)  # Output: 0
print("my_range.sto: ", my_range.stop)  # Output: 5
print("my_range.step: ", my_range.step)  # Output: 1
print() # newline

# Bytes
my_bytes = b'Hello'
print("my_bytes = b'Hello'")
print("type(my_bytes): ", type(my_bytes))  # Output: <class 'bytes'>
# Bytes methods
print("len(my_bytes): ", len(my_bytes))  # Output: 5
print("my_bytes.decode(): ", my_bytes.decode())  # Output: "Hello"
print("my_bytes.hex(): ", my_bytes.hex())  # Output: "48656c6c6f"
print() # newline

# Complex
my_complex = 3 + 4j
print("my_complex = 3 + 4j")
print("type(my_complex): ", type(my_complex))  # Output: <class 'complex'>
# Complex methods
print("my_complex.real: ", my_complex.real)  # Output: 3.0
print("my_complex.imag: ", my_complex.imag)  # Output: 4.0
print("my_complex.conjugate(): ", my_complex.conjugate())  # Output: (3-4j)
print() # newline

# None
my_none = None
print("my_none = None")
print("type(my_none): ", type(my_none))  # Output: <class 'NoneType'>
# None methods
print("my_none is None: ", my_none is None)  # Output: True
