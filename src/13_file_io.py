"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt') as foo:
    print(foo.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as bar:
    # Figured out how to do this via this stackoverflow comment:
    # https://stackoverflow.com/a/16162599/12685847
    # Note that there can't be a line break after the triple-apostrophes
    # or else the first line in bar.txt will be a blank line.
    content = '''This file is named "bar."
Humanity is drowning in #content.
This is just one more droplet in the flood.'''
    bar.write(content)
