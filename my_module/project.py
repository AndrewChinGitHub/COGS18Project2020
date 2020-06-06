"""
Name: Andrew Chin
File: project.py 
Description: Stack implementation that uses numpy arrays. Includes the 
             traditional push, pop, peek methods.
Imports: Numpy 
"""
import numpy as np

class Stack():
    """
    >>> stack = Stack(3)
    >>> isinstance(stack.items, np.ndarray)
    True
    >>> stack.nelem
    0
    >>> print(stack)
    (bottom)(top)
    >>> stack.push(1)
    >>> stack.push(2)
    >>> print(stack)
    (bottom) 1 -> 2 (top)
    >>> stack.pop()
    2
    >>> print(stack)
    (bottom) 1 (top)
    >>> stack.pop()
    1
    >>> stack.pop()
    'No elements to remove'
    >>> stack.push(5)
    >>> stack.push(10)
    >>> stack.push(15)
    >>> stack.push(20)
    'No space to add elements'
    >>> print(stack)
    (bottom) 5 -> 10 -> 15 (top)
    >>> stack.peek()
    15
    >>> print(stack)
    (bottom) 5 -> 10 -> 15 (top)
    """
    """
    Constructor for the Stack class
    @params: int 
    """
    def __init__(self,int):
        self.items = np.array([])
        self.nelem = len(self.items)
        self.limit = int
        self.front = 0
        self.rear = 0
        
    """
    String method that when called, returns a printed stack denoted by 
    '(bottom)-->(elem) --> ... -->(top)'
    """
    def __str__(self):
        if len(self.items) == 0:
            return '(bottom)(top)'
        string = ''
        for i in range(len(self.items)-1): #simple loop to loop through elems
            if isinstance(self.items[i],(int,float)):
                string+=str(int(self.items[i])) + ' -> '
            else:
                string+=str(self.items[i]) + ' -> '
        string += str(int(self.items[-1]))
        return '(bottom) {} (top)'.format(string) #string formatter 
        
    """
    Method 'stacks' another elem at the top of the stack. 
    @param elem: elem to add to the stack
    """
    def push(self, elem):
        if len(self.items) >= self.limit: #Checks if theres space in stack
            return 'No space to add elements'
        else: #No space in stack
            self.items = np.append(self.items,elem)
            
    """
    Method that removes the top elem of the stack and returns 
    removed elem.
    @params NA
    @return elem at the top of the stack
    """
    def pop(self):
        if len(self.items) == 0: #if stack is empty, do nothing
            return 'No elements to remove'
        else: #stack has >=1 elems
            elem = self.items[-1] #takes top elem
            self.items = self.items[:-1] #reassigns rest of stack 
            if isinstance(elem,float) == True:
                return int(elem)
            else:
                return elem
                
    """
    Method takes a look at the top elem of the stack, 
    but does not remove it from the stack. Returns the top elem.
    @params NA
    @return elem at the top of the stack
    """
    def peek(self):
        if len(self.items) == 0:
            return 'No elements to remove'
        elem = self.items[-1]
        if isinstance(elem,float) == True:
            return int(elem)
        else:
            return elem 
              
    """
    Checks the size of the stack (number of elements in the stack) 
    and returns that number.
    @params NA
    @return size of the stack (int)
    """
    def size(self):
        return len(self.items)
        
    """
    Checks to see if the stack has any elems in it or not. True if 
    nothing is in the stack, False otherwise.
    @params NA
    @return bool True or False according to method description 
    """
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
