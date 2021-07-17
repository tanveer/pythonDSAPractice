class Node:
    # constructor method
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    # constructor method
    def __init__(self):
        self.head = None

    # return the size of the linked list
    def size(self):
        if not self.head:
            return 0
        else:
            count = 0
            node = self.head
            while node:
                count += 1
                node = node.next
            return count

    # get first node
    def getFirst(self):
        return self.getAt(0)

    # get last node
    def getLast(self):
        return self.getAt(self.size() - 1)

    # get node at a specific position
    def getAt(self, pos):
        if pos == 0:
            return self.head

        curr = self.head
        currPosition = 0
        while curr:
            if currPosition == pos:
                return curr

            currPosition += 1
            curr = curr.next
        return None

    # insert node
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    # insert node at a specific postion
    def insertAt(self, pos, data):
        # if head is null make head from data and return
        if not self.head:
            self.head = Node(data)
            return

        # if pos is 0 then update head
        if pos == 0:
            # update head and move current head to head.next
            self.head = Node(data, self.head)
            return

        previous = self.getAt(pos - 1) or self.getLast()
        newNode = Node(data, previous.next)
        previous.next = newNode

    # insert node at first position
    def insertFirst(self, data):
        self.insertAt(0, data)

    # insert node at last position
    def insertLast(self, data):
        if not self.head:
            self.insertAt(0, data)
            return

        lastNode = self.getLast()
        if lastNode:
            lastNode.next = Node(data)

    # remove first node
    def removeFirst(self):
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None

    # remove last node
    def removeLast(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        prev = self.head
        node = prev.next
        while node.next:
            prev = node
            node = node.next
        prev.next = None

    # reomve node at given position
    def removeAt(self, pos):
        if not self.head:
            return

        if pos == 0:
            self.head = self.head.next
            return

        previous = self.getAt(pos - 1)
        if not previous or not previous.next:
            return

        previous.next = previous.next.next
