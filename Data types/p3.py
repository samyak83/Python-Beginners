'''
Data Types in Python
=====================
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview'''

x = 5
print(type(x))

##############################################

d1 = "Hello World"	#string data type
print(d1)

d2 = 20	    #int data type
print(d2)

d3 = 20.5	 #float data type
print(d3)

d4 = 1j     #complex data type
print(d4)

d5 = ["apple", "banana", "cherry"]	#list data type
print(d5)

d6 = ("apple", "banana", "cherry")	#tuple data type
print(d6)

d7 = range(6)	#range data type
print(d7)

d8 = {"name" : "John", "age" : 36}	#dict data type
print(d8)

d9 = {"apple", "banana", "cherry"}	#set data type
print(d9)

d10 = frozenset({"apple", "banana", "cherry"})	#frozenset data type
print(d10)

d11 = True	#bool data type
print(d11)

d12 = b"Hello"	#bytes data type
print(d12)

d13 = bytearray(5)	#bytearray data type
print(d13)

d14 = memoryview(bytes(5))	#memoryview data type
print(d14)