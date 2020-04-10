"""Linked List implementation in Python"""


class LinkedList:
    """Class for Linked List and its methods"""
    def __init__(self):
        """Initialize the head of Linked List with None"""
        self.head = None

    def append(self, node):
        """
        Method to add a node to the end of the linked list
        :param node: Node to be added
        :return: none
        """
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        else:
            self.head = node

    def pop(self):
        """
        Method to remove node from the end of the list
        :return: None
        """
        if not self.head:
            print('List is empty')
            return
        current_node = self.head
        if not current_node.next:
            self.head = None
            return
        previous_node = None
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None

    def prepend(self, node):
        """
        Method to add node to the start of the list
        :param node: Node to be added
        :return: None
        """
        if not self.head:
            self.head = node
            return

        temp_node = self.head
        node.next = temp_node
        self.head = node

    def remove_head(self):
        """Remove the head of the list"""
        if not self.head:
            print('Empty List')

        self.head = self.head.next

    def remove(self, node):
        """
        Remove a specific node from the Linked List
        :param node: Node to be removed
        :return: None
        """
        if not self.head:
            print('Empty List')
            return

        if self.head.data == node.data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == node.data:
                if current_node.next.next:
                    current_node.next = current_node.next.next
                    return
                else:
                    current_node.next = None
                    return
            current_node = current_node.next
        print('Node not found')

    def insert(self, node, index=None):
        """
        Method to insert node at a specific index
        :param index:
        :param node
        :return:
        """

        if not self.head:
            print("List is empty")
            return

        if not index:
            self.prepend(node)
            return

        i = 1
        previous_node = self.head
        current_node = previous_node.next
        while current_node:
            if index == i:
                previous_node.next = node
                node.next = current_node
                return
            i = i+1
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = node

    def print_list(self):
        """
        Print the linked list
        :return:
        """
        current_node = self.head
        if not current_node:
            print('List is empty.')
            return

        while current_node:
            print(current_node.data)
            current_node = current_node.next


class Node:
    """ Node class """
    def __init__(self, data):
        self.data = data
        self.next = None


ll = LinkedList()

ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(5))
ll.append(Node(6))
# ll.prepend(Node(5))
ll.print_list()
# ll.remove_head()
ll.remove(Node(1))
ll.print_list()
ll.remove(Node(5))
ll.remove(Node(8))
ll.append(Node(7))
ll.append(Node(8))

ll.insert(Node(10), 3424)

ll.print_list()
