#dictionaries
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#iteration over dictionaries
for name, number in phonebook.items(): 
    print("Phone number of %s is %d" % (name, number))

#removing items with pop()
phonebook.pop("John")
print(phonebook)

#removing items with del
del phonebook["Jill"]
print(phonebook)

#adding jake to phonebook
phonebook["Jake"] = 938273443

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")