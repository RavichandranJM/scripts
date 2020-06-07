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

a = Item("A", "a")
b = Item("B", "b")
c = Item("C", "c")
l = ListBox()
l.add(a, b, c)
l.count()

d = DictBox()
d.add(b, c)
d.count()

