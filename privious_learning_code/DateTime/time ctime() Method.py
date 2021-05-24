
# Description
#
# The method ctime() converts a time expressed in seconds since the epoch to a string representing local time. If secs is not provided or None, the current time as returned by time() is used. This function is equivalent to asctime(localtime(secs)). Locale information is not used by ctime().
# Syntax
#
# Following is the syntax for ctime() method −
#
# time.ctime([ sec ])
#
# Parameters
#
# sec − These are the number of seconds to be converted into string representation.
#
# Return Value
#
# This method does not return any value.
# Example
import time

print("time.ctime() : %s" % time.ctime())