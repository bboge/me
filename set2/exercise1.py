"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this creates a list called 'some_words' that contains: 'what', 'does', 
# 'this', 'line', 'do' and '?'.
some_words = ["what", "does", "this", "line", "do", "?"]

# I think that this assigns each string in the 'some_words' to 'word' using a for loop.
for word in some_words:
    # I think that this will print each string in the list individually, as 'word' represents
    # every word is the list.
    print(word)

# I think that this will perform the same action as line 25, but assigns each string as 'x'
# rather than 'word'.
for x in some_words:
    # I think that this will again print out each string in 'some_words' individually.
    print(x)

# I think that this line will print "["what", "does", "this", "line", "do", "?"]".
print(some_words)

# I think that this will print the phrase 'some_words contains more than 3 words' if there are
# more than 3 words in the list.
if len(some_words) > 3:
    print("some_words contains more than 3 words")

# I think this begins defining a fuction called 'usefulfuction()'.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # I think this defines the function that will print five attributes about the users sysytem:
    # sysname, nodename, release, version, and machine.
    print(platform.uname())

# I think this will call the fuction and print 'platform.uname()'.
usefulFunction()
