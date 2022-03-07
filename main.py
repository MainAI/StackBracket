class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        if len(self.item) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.item.append(element)

    def pop(self):
        if self.isEmpty() is False:
            upper = self.item.pop(-1)
            return upper
        else:
            return None

    def peek(self):
        if self.isEmpty() is False:
            el_upper = self.item[-1]
            return el_upper
        else:
            return None

    def size(self):
        length = len(self.item)
        return length


def check_bracket(list_bracket):
    """
       check the balance of brackets (list_bracket)
       possibility of other characters between brackets
    """
    dict_bracket = {"(": ")", "{": "}", "[": "]"}
    bracket_stack = Stack()
    for element in list_bracket:
        if element in dict_bracket.keys():
            bracket_stack.push(element)
        elif element == dict_bracket.get(bracket_stack.peek()):
            bracket_stack.pop()
        else:
            if element in dict_bracket.values():
                return print("Несбалансированно")
            else:
                continue
    if bracket_stack.isEmpty() is True:
        return print("Сбалансированно")


if __name__ == '__main__':
    data = input("Enter data:")
    check_bracket(data)
