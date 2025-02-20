# Description
#
# The method mktime() is the inverse function of localtime(). Its argument is the struct_time or full 9-tuple and it returns a floating point number, for compatibility with time().
#
# If the input value cannot be represented as a valid time, either OverflowError or ValueError will be raised.
# Syntax
#
# Following is the syntax for mktime() method −
#
# time.mktime(t)
#
# Parameters
#
# t − This is the struct_time or full 9-tuple.
#
# Return Value
#
# This method returns a floating point number, for compatibility with time().
# Example
import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime(t)
print("time.mktime(t) : %f" % secs)
print("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))
