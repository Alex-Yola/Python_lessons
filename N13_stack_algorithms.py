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


def checking_braces(s):
    """Проверка последовательности скобок на закрытие.
    Возвращает соответственно либо True, либо Folse.
    """
    a = Stack()
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            a.push(brace)
        else:
            if a.isEmpty():
                return False
            left = a.pop()
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return a.isEmpty()

def test_checking_braces():
    print(checking_braces("__(_[(-(_))]_)__"))
    print(checking_braces("__)_[(-(_))]_)__"))
    print(checking_braces("__(_[(-(_))]_))__"))

test_checking_braces()


def Reverse_Polish_notation(s):
    """Вычисляет выражение, заданное обратной польской нотацией.
    Например: [2,3,4,"*","-"] <=> 2-3*4=-10 , [2,3,"+",4,"*"] <=> (2+3)*4=20
    """
    stk = Stack()
    for a in s:
        if type(a) is not str:
            stk.push(a)
        else:  ## символ операции
            x2 = stk.pop()
            x1 = stk.pop()
            z = eval(str(x1) + a + str(x2))
            stk.push(z)
    return stk.pop()

def test_Reverse_Polish_notation():
    print('[2,3,4,"*","-"] <=> 2-3*4 =', Reverse_Polish_notation([2,3,4,"*","-"]))
    print('[2,3,"+",4,"*"] <=> (2+3)*4 =', Reverse_Polish_notation([2,3,"+",4,"*"]))

test_Reverse_Polish_notation()