class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def get_from_stack(self, elem):
        for it in range(len(self._items)):
            dl = []
            ind = self.pop()
            if elem != ind:
                dl.append(ind)

            elif elem == ind:
                for el in dl:
                    self.push(el)
                return elem

        raise ValueError('Element not found')

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    stack = Stack()
    item = [1, 89, 65, 36, 56, 84, 56, 325, 45, 25, 48]
    for elem in item:
        stack.push(elem)

    print(stack.get_from_stack(2))