class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self) -> int:
        return len(self.items)

def is_balanced(expression: str) -> bool:
    stack = Stack()
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets:
            if stack.is_empty() or brackets[char] != stack.pop():
                return False

    return stack.is_empty()

# Примеры сбалансированных последовательностей скобок
print(is_balanced("(((([{}]))))"))  # Truee
print(is_balanced("[([])((([[[]]])))]{()}"))  # True
print(is_balanced("{{[()]}}"))  # True

# Примеры несбалансированных последовательностей скобок
print(is_balanced("(()"))  # False
print(is_balanced("([)]"))  # False
print(is_balanced("{{}"))  # False