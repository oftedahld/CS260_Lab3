#2 classes, TextLink & TextClass
"""
class Link
 // data contained in link
 int value

 // reference to the next link in the list
 Link next

 // reference to the previous link in the list
 Link prev

class Deque:
    def __init__(self, arraySize = 20):
        if arraySize < 1:
            size = 20
        self.size = arraySize
        self.headIndex = 0
        self.tailIndex = 0
        self.elementsCount = 0
        self.isWrapped = False
        self.theArray = [0] * arraySize
 """

class TextLink:
    def __init__(self, value, nextLink="", prevLink=""):
        """Creates a double-pointed link with null pointers if not specified"""
        self.value = value
        self.next = nextLink
        self.prev = prevLink

 