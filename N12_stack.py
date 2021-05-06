class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)

def test_Stack():
    s = Stack()
    print("s.size():", s.size())
    print("s.isEmpty()", s.isEmpty())
    s.push("a")
    s.push("b")
    s.push("c")
    print("s.peek():", s.peek())
    print("s.size():", s.size())
    print("s.isEmpty():", s.isEmpty())
    print("s.pop():", s.pop())
    print("s.pop():", s.pop())
    print("s.pop():", s.pop())
    print("s.size():", s.size())
    print("s.isEmpty():", s.isEmpty())

test_Stack()
