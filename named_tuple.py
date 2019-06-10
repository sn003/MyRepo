"""
Below examples discusses about namedtuple from collections module
"""
import collections

#Declaring a namedtuple
employee = collections.namedtuple("Employee", ["Name", "Age", "DOB"])

#Adding Values
emp = employee("Johnny Depp", "35", "02011983")

#initializing iterable
ex_list = ["Abraham", "24", "20091994"]

#initializing dict
ex_dict = {"Name" : "Moti", "Age" : 29, "DOB" : "16091987"}

#Below 3print statements print Same output
print(emp.Name) #Access by key
print(emp[0]) #Access by index
print(getattr(emp, "Name")) #Access via getattr


#using _make() to return namedtuple()
print ("The namedtuple instance using iterable is : ")
print(employee._make(ex_list))

#using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is :")
print(emp._asdict())


#using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is :")
print(employee(**ex_dict))


#print fields of the named tuple
print(emp._fields)
