"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module import project
##
##

def test1():
    stack = project.Stack()
    stack.push(1)
    assert stack.pop() == 1

def test2():
    stack = project.Stack()
    assert stack.peep() == 'No elements to remove'
    



                 
    