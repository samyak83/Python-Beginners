#Assign String to a Variable
str = 'hello'
print(str)

###############################

#Multiline Strings
str2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""  #three double quotes
print(str2)

str3 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''' #three single quotes
print(str3)
##################################

#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

###################################

#Get the characters from position 2 to position 5 (not included):
#Slicing
b = "Hello, World!"
print(b[2:5])

###################################

#Negative Indexing
#Get the characters from position 5 to position 1, starting the count from the end of the string:
c = "Hello, World!"
print(c[-5:-2])

####################################

#String Length
#The len() function returns the length of a string:
d = "Hello, World!"
print(len(d))

####################################

#The strip() method removes any whitespace from the beginning or the end:
e = " Hello, World! "
print(e.strip()) # returns "Hello, World!"

#The lower() method returns the string in lower case:
print(e.lower())

#The upper() method returns the string in upper case:
print(e.upper())

#The replace() method replaces a string with another string:
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(",")) # returns ['Hello', ' World!']

#To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
txt = "The rain in Spain stays mainly in the plain"
check = "ain" in txt
print(check)

check2 = "ain" not in txt
print(check2)

#string Concatenation
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print(s3)

s4 = s1 + " " + s2
print(s4)

#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
qua = 3
item_no = 567
price_ = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(qua, item_no, price_))

'''
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value '''

'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning//'''



