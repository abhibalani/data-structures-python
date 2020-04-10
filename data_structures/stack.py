"""Stack implementation in Python"""


class Stack:
    """Class for stack and its methods"""
    def __init__(self):
        """Initialize the top of stack to none"""
        self.top = None

    def push(self, node):
        """
        Method to push a node into a stack
        :param node: Node to be pushed
        :return: None
        """
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node

        return

    def pop(self):
        """
        Method to pop the value from top of the stack
        :return: return the value which is popped
        """
        if not self.top:
            print('Stack is empty')
            return
        value = self.top.data
        self.top = self.top.next
        print('Value popped is: ', value)
        return value

    def print_stack(self):
        """Method to print the stack"""
        current = self.top
        while current:
            print(current.data)
            current = current.next

        return


class Node:
    """Class for Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


stack = Stack()
stack.print_stack()
stack.push(Node(1))
stack.push(Node(2))
stack.push(Node(3))
stack.push(Node(4))
stack.push(Node(5))
stack.print_stack()
stack.pop()
stack.pop()
stack.pop()
stack.print_stack()
stack.pop()
stack.pop()
stack.print_stack()
stack.pop()
stack.pop()

stack.print_stack()

