# Run the script like:
# user$ python3 basic_arguments.py 1 2
# or
# user$ python3 basic_arguments.py 2 3 "Test"

# basic command line treatment can be done with the
# sys module:
import sys

# command line arguments given to a script are provided
# after the script call in the list 'sys.argv':
print(type(sys.argv), len(sys.argv))

# print command line arguments:
# Note that the first element (index 0) in the sys.argv-list
# contains the call to the script (script name and program path):
for arg in sys.argv:
    # the elemenrs of the sys.argv list are all strings!
    # You need to explicitely cast them to other types if
    # you need to (e.g. numbers to int/float) if you want to
    # perform calculations.
    print(arg, type(arg))
