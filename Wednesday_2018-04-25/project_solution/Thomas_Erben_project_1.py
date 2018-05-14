def cesar_crypt(text, shift):
    """
    En- or decryt some text with the cesar cipher

    input: - the text to be decrypted or encryped
           - the shift to be applied to individual letters
             (give a negative number to decrypt text that
             was encrypted with a corresponding positive
             shift)
    return: de/encrypted text as a string

    REMARK:
    We assume that the text only consists of lower case letters
    and spaces. We do not verify this!
    """

    result = "" # resulting de/encoded text

    for letter in text:
        # treat spaces separately
        if letter == " ":
            result = result + " "
        else:
            # The letter 'a' is represented with the ASCII-number 97
            # and so on. We work with numbers 0-25 for the 26
            # letters (a-z) of the alphabet:
            number = ord(letter) - 97

            # shift the number taking into account wrap-arounds before 'a'
            # and after 'z':
            number = (number + shift) % 26

            result = result + chr(number + 97)

    return result

# decrypt the given string from the project sheet:
test_str = 'pbatenghyngvbaf lbh unir fhpprrqrq va qrpelcgvat gur fgevat'
print(cesar_crypt(test_str, -13))

# decrypt the given string and find the shift; we do this by just trying
# all shifts and verifying when the result makes sense :-)
test_str = 'gwc uivioml bw nqvl bpm zqopb apqnb'
shift = 0
while shift >= -25:
    print(shift, cesar_crypt(test_str, shift))

    shift = shift - 1

# obviously the string was decrypted with a shift of 8 characters.
