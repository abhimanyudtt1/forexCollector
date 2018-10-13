import enum


class selectors(object):

    def __init__(self,type,selector):
        self.type = type
        self.selector = selector

    def __init__(self):
        self.type = None
        self.selector = None

    def withType(self,type):
        self.type = type
        return self

    def withSelector(self,selector):
        self.selector = selector
        return self

    def getType(self):
        return self.type

    def getSelector(self):
        return self.selector




