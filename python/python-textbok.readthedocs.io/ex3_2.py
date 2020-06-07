#!/usr/bin/python3
class Box(object):
    def add(self, *items):
        raise NotImplementedError
    def empty(self):
        raise NotImplementedError
    def count(self):
        raise NotImplementedError

class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class ListBox(Box):
    def __init__(self):
        self._items = []
    def add(self, *items):
        print(*items)
        self._items.extend(items)
    def empty(self):
        items = self._items
        self._items = []
        return items
    def count(self):
        return len(self._items)

class DictBox(Box):
    def __init__(self):
        self._items = {}
    def add(self, *items):
        self._items.update(dict((i.name, i) for i in items))
    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items
    def count(self):
        return len(self._items)

def repackBoxes(*boxes):
    items = []
    for box in boxes:
        items.extend(box.empty())

    while items:
        for box in boxes:
            try:
                box.add(items.pop())
            except IndexError:
                break


def getItems(length):
    items = []
    for num in range(length):
        items.append(Item(str(num), num))
    return items

box1 = ListBox()
#box1.add(*getItems(20))
box1.add(*(Item(str(i), i) for i in range(20)))

box2 = ListBox()
#box2.add(*getItems(9))
box2.add(*(Item(str(i), i) for i in range(9)))

box3 = DictBox()
#box3.add(*getItems(5))
box3.add(*(Item(str(i), i) for i in range(5)))

repackBoxes(box1, box2, box3)
print(box1.count())
print(box2.count())
print(box3.count())
