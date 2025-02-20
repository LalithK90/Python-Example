
# Description
#
# The method cmp() compares elements of two lists.
# Syntax
#
# Following is the syntax for cmp() method −
#
# cmp(list1, list2)
#
# Parameters
#
# list1 − This is the first list to be compared.
#
# list2 − This is the second list to be compared.
#
# Return Value
#
# If elements are of the same type, perform the compare and return the result. If elements are different types,
# check to see if they are numbers.
#
# If numbers, perform numeric coercion if necessary and compare.
# If either element is a number, then the other element is "larger" (numbers are "smallest").
# Otherwise, types are sorted alphabetically by name.
#
# If we reached the end of one of the lists, the longer list is "larger." If we exhaust both lists and share the same
# data, the result is a tie, meaning that 0 is returned. Example
from filecmp import cmp

list1, list2 = [123, 'xyz'], [456, 'abc']
print(cmp(list1, list2))
print(cmp(list2, list1))
list3 = list2 + [786];
print(cmp(list2, list3))