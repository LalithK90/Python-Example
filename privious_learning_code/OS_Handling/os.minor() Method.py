
# Description
#
# The method minor() extracts the device minor number from a raw device number (usually the st_dev or st_rdev field from stat).
# Syntax
#
# Following is the syntax for minor() method −
#
# os.minor(device)
#
# Parameters
#
# device − This is a raw device number (usually the st_dev or st_rdev field from stat).
#
# Return Value
#
# This method returns the device minor number.
# Example
import os, sys

path = "/var/www/html/foo.txt"

# Now get the touple
info = os.lstat(path)

# Get major and minor device number
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print("Major Device Number :", major_dnum)
print("Minor Device Number :", minor_dnum)