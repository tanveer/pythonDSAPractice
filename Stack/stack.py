"""
    Implement stack class with basic stack operation 'Push, Pop, Peek, Size, Empty'
    create both using Array list and Linked list 
"""

# Stack using Python's built in list / array data structure


class Stack:
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.storage:
            return self.storage.pop()
        return None

    def peek(self):
        if self.storage:
            return self.storage[-1]
        return None

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        if self.storage:
            return len(self.storage)
        return None


# implementation of stack using linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackWithLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        if not self.top:
            self.top = Node(value)
            self.size += 1
            return
        else:
            previouse = self.top
            self.top = Node(value)
            self.top.next = previouse
        self.size += 1

    def peek(self):
        if not self.top:
            return None

        return self.top.value

    def pop(self):
        if not self.size:
            return None

        removeTop = self.top
        self.top = removeTop.newNode
        value = removeTop.value
        removeTop = None
        self.size -= 1
        return value

    def isEmpty(self):
        return self.size == 0


"""
 most common stack based interview questions
"""

# reverse a given string


def reverse(str):
    stack = Stack()
    reversed = []
    for char in str:
        stack.push(char)
        reversed.append(stack.pop())
    return ''.join(reversed)


"""
this is a classic interview queston asked by many top companies
Cheack if the brackets are balance return True or False 
this could be implemented in many different ways 
here is one of the many simple & more readable approachs
"""

# variables to help make code cleaner and easy to read
leftBracket = ['(', '[', '{', '<']
rightBracket = [')', ']', '}', '>']

# helper methods to make code more readable and easy to understand


def isLeftBracket(bracket):
    return bracket in leftBracket


def isRightBracket(bracket):
    return bracket in rightBracket


def isBracketMatch(left, right):
    return isLeftBracket(left) and isRightBracket(right)


def balanceBracket(str):
    # uncomment line below to test
    # stack = Stack()

    # comment the line blelow when testing with Stack() using list/array imeplementation
    stack = StackWithLinkedList()

    if not str:
        return False

    for bracket in str:
        if isLeftBracket(bracket):
            stack.push(bracket)

        if isRightBracket(bracket):
            top = stack.pop()
            if not isBracketMatch(top, bracket):
                return False
    return stack.isEmpty()
