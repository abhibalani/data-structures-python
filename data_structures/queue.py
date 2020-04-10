"""Queue implementation in Python"""


class Queue:
    """Class for queue and its methods"""
    def __init__(self):
        """Initialize the queue head"""
        self.head = None

    def push(self, node):
        """
        Push the node inside queue
        :param node: node to be pushed
        :return: None
        """
        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def pop(self):
        """
        Method to remove first element from queue
        :return: value of removed element
        """
        if not self.head:
            print('Queue is Empty')
            return
        value = self.head.data
        self.head = self.head.next
        print('Value removed is: ', value)
        return value

    def print_queue(self):
        """Method to print the queue"""
        if not self.head:
            print('Empty queue')
            return

        current = self.head
        while current:
            print(current.data)
            current = current.next

        return


class Node:
    """Class for Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


q = Queue()
q.print_queue()

q.push(Node(1))
q.push(Node(2))
q.push(Node(3))
q.push(Node(4))
q.push(Node(5))
q.print_queue()

q.pop()
q.pop()
q.pop()
q.print_queue()

q.pop()
q.pop()
q.print_queue()

q.print_queue()
