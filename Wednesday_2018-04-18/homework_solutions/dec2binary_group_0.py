n = 123456789  # we want to represent 'n' as binyray number
b = "" # the binary representation will be stored as a string.
       # (here initialised to an empty string)

n_orig = n # we modify n below but we need the original value for
           # the result printout.

# We need to treat the special case n=0 separately!
# I guess that this will be one of the major difficulties for the
# students!
if n == 0:
    b = "0"
else:
    while n != 0:
        n, r = divmod(n, 2)
        b = str(r) + b

print("binary representation of", n_orig, "is", b)
