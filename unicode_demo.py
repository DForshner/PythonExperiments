# -*- coding: utf-8 -*-

"""
Tutorial on unicode in python 2.7
"""

# extra fun
u = "idzie wąż wąską dróżką"
uu = u.decode("utf8")
s = uu.encode("cp1250")
print(s)

# Strings aren"t a list of characters they are binary data.
print "@ symbol as ASCII Hex: \x40"
print "@ symbol as ASCII Octal: \100"
print "null char \x00  is ok"

# Unicode strings in python are not binary data they are a list of characters that
# can be represented as binary data in a variety of ways.  To do anything with unicode
# strings they must first be converted into a binary representation (like utf-8).
print u"hello kitty".encode("utf-8")
print u"hello \u0040 unicode \u5b57".encode("utf-8")
print u"\u5b57".encode("utf-8")

# You can differentiate between these two types of strings
assert type(u"\u5b57") is unicode
assert isinstance(u"u5b57", unicode)
assert not isinstance(u"u5b57", str)
assert isinstance(u"u5b57".encode("utf-8"), str)
assert isinstance(u"u5b57", basestring)
assert isinstance("\xe5\xad\x97", basestring)

# UTF-8 is the most commonly used encoding and is backwards compatible with ASCII
assert u"@".encode("ascii") == "@"
assert u"@".encode("utf-8") == "@"
assert hex(ord("@")) == "0x40"
print("\x40")
print(u"\x40")

# Other encodings like UTF-16 are not compatible with ASCII
assert not u"@".encode("utf-16") == "@"

# It can take between one and size bytes to represent a single character in UTF-8.
assert len(u"\u5b57") == 1
assert len("\xe5\xad\x95") == 3
assert len("\xe5\xad\x95".decode("utf-8")) == 1

# UTF-8 isn"t very efficient at storing Asian symbols, taking a whole three bytes
# so they have created their own encodings like big5.
assert len(u"\u5b57".encode("utf-8")) == 3
assert len(u"\u5b57".encode("big5")) == 2

# When accepting data over the network we can receive invalid characters that can cause exceptions.
try:
    good_utf = u"\u0040 and \u5b57 look good".encode("utf-8")
    bad_utf = "\xff\xff\xff"
    (good_utf + bad_utf).decode("utf-8")
except UnicodeDecodeError:
    print("Need a better decoding ring.")

print((good_utf + bad_utf).decode("utf-8", "replace"))  # Show unknown symbol placeholder
print((good_utf + bad_utf).decode("utf-8", "ignore"))  # Don"t show anything at all

# Python assumes all characters are ASCII unless told otherwise

import sys
assert sys.getdefaultencoding() == "ascii"

try:
    with open("/tmp/lol", "wb") as f:
        f.write(u"\u5b57")
except UnicodeEncodeError:
    print("Still Need a better decoding ring.")

# We could encode our data
with open("/tmp/lolcat", "wb") as f:
    f.write(u"\u5b57".encode("utf-8"))
with open("/tmp/lolcat", "rb") as f:
    utf8_data = f.read()
    assert utf8_data.decode("utf-8") == u"\u5b57"

# or we could make life easier and use codecs
import codecs
with codecs.open("/tmp/lolcat", "wb", "utf-8") as f:
    binary_data = u"\u5b57"
    assert isinstance(binary_data, unicode)
    f.write(binary_data)
with codecs.open("/tmp/lolcat", "rb", "utf-8") as f:
    utf8_data = f.read()
    assert utf8_data == u"\u5b57"

# Don"t write binary strings with non-ascii data
with codecs.open("/tmp/lolcat", "wb", "utf-8") as f:
    binary_data_ascii = "I'm 100% ascii"
    assert isinstance(binary_data_ascii, str)
    f.write(binary_data_ascii)

try:
    with codecs.open("/tmp/lolcat", "wb", "utf-8") as f:
        binary_data_not_ascii = "\xe5\xad\x97"
        assert isinstance(binary_data_not_ascii, str)
        f.write(binary_data_not_ascii)
except UnicodeDecodeError:
    print("Again with decoding problems?")

# The default encoding on windows machines is often latin-1 but you may want to convert to utf-8.
pretend = "Pretend latin-1 data from windows".encode("latin-1")
works_everywhere = pretend.decode("latin-1")

# You can put u in front of ascii only strings and Python will turn binary strings to
# unicode strings automatically.
assert isinstance(("hello" + "there"), str)
assert isinstance(("hello" + u"there"), unicode)

# But exceptions happen non-ascii characters in non unicode strings are passed to libraries
# It"s safest to put all non-ascii characters in unicode stings before passing them to
# Python libraries.
try:
    assert isinstance(("hello " + "André"), str)
    ("hello " + "André").encode("utf-8")
except UnicodeDecodeError:
    print(":-(")

# This could crash if python can't figure out the encodings supported by the terminal
try:
    print(u"hello @ unicode 字")
except UnicodeEncodeError:
    print("failed?")

# This is safer because pretty much everything supports utf-8
print(u"hello @ unicode 字".encode('utf-8'))

# Python will assume byte strings are ASCII when they reach standard I/O
try:
    print("hello @ unicode 字")
except UnicodeEncodeError:
    print("failed?")

# Make sure your web application's form inputs are in UTF-8 by adding the following to the <head> section
# <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
# Remember that HTML defines unicode entities in base ten decimal so you may need to convert them to hex.
print(hex(0214))
