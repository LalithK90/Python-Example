# Description
#
# The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.
# Syntax
#
# Following is the syntax for setdefault() method −
#
# dict.setdefault(key, default=None)
#
# Parameters
#
# key − This is the key to be searched.
#
# default − This is the Value to be returned in case key is not found.
#
# Return Value
#
# This method returns the key value available in the dictionary and if given key is not available then it will return provided default value.
# Example
dict = {'Name': 'Zara', 'Age': 7}
print("Value : %s" % dict.setdefault('Age', None))
print("Value : %s" % dict.setdefault('Sex', None))
