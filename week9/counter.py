#!/usr/bin/env python3

class Counter:

    def __init__(self, data, pattern=None):
        self.data = tuple(data)
        self.pattern = [str(i) for i in pattern] if pattern else None
        self.collection = dict()
        if self.pattern:
            self.matching()
        else:
            self.count()

    def count(self):
        # if data is string or list
        for item in self.data:
            item = str(item)  # just for consistency
            if item in self.collection:
                self.collection[item] += 1
            else:
                self.collection[item] = 1

    def matching(self):
        # if data is string or list
        for item in self.data:
            item = str(item)  # just for consistency
            if item in self.pattern:
                if item in self.collection:
                    self.collection[item] += 1
                else:
                    self.collection[item] = 1

    def duplicates(self):
        c = self.collection
        return {i:c[i] for i in c if c[i] > 1}

    def uniques(self):
        c = self.collection
        return {i:c[i] for i in c if c[i] == 1}
