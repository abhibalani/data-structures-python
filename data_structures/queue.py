"""Queue implementation in Python"""


class Queue:
    """Class for queue and its methods"""
    def __init__(self):
        """Initialize the queue head"""
        self.head = None

    def enqueue(self, node):
        """
        Add the node inside queue
        :param node: node to be enqueued
        :return: None
        """
        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def dequeue(self):
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

    def peek(self):
        """

        :return:
        """
        current_node = self.head
        previous_node = current_node

        while current_node:
            previous_node = current_node
            current_node = current_node.next

        return previous_node

    def __len__(self):
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count+=1

        return count


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

q.enqueue(Node(1))
q.enqueue(Node(2))
q.enqueue(Node(3))
q.enqueue(Node(4))
q.enqueue(Node(5))
print('Length of queue is: ',  str(len(q)))
q.print_queue()

q.dequeue()
q.dequeue()
q.dequeue()
q.print_queue()

q.dequeue()
q.dequeue()
q.print_queue()

q.print_queue()
