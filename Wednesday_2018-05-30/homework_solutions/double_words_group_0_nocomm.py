import sys
import string
import re

if len(sys.argv) != 2:
    print("Synopsis: %s file" % (sys.argv[0]), file=sys.stderr)
    sys.exit(1)

txtfile = open(sys.argv[1], 'r')
line_number = 1
last_word = ""

for line in txtfile:
    words = re.split('\W+', line.rstrip())
    words = [ word for word in words if word != "" ]

    if len(words) > 0:
        for i in range(1, len(words)):
            if words[i] == words[i - 1]:
                print("Repetition in line %d. Word \"%s\" at position %d!" % \
                      (line_number, words[i -1], i))

        if line_number > 1:
            if words[0] == last_word:
                print("Repetition of the first word \"%s\" on line %d." % \
                      (last_word, line_number), end=' ')
                print("It occured at the end of the previous (non-empty) line!")

        last_word = words[-1]
    line_number = line_number + 1

txtfile.close()
