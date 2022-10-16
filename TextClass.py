#2 classes, TextLink & TextClass
"""
class Link
 // data contained in link
 int value

 // reference to the next link in the list
 Link next

 // reference to the previous link in the list
 Link prev

class Link  
        // data contained in link 
        int value 
     
        // reference to the next link in the list 
        Link next 
     
        // reference to the previous link in the list 
        Link prev 
     
    public: 
    // constructor 
    Link(int value, Link next = nullptr, Link prev = nullptr) 
        this->value = value 
        this->next = next 
        this->prev = prev 

    // access methods 
        int getValue()  
            return this->value 
         
        Link getNext()  
            return this->next 
         
        Link getPrev()  
            return this->prev 
         
        void setNext(Link next)  
            this->next = next 
         
        void setPrev(Link prev)  
            this->prev = prev   
 """

from operator import truediv


class TextLink:
    def __init__(self, value, nextLink=None, prevLink=None):
        """Creates a double-pointed link with null pointers if not specified"""
        self.value = value
        self.next = nextLink
        self.prev = prevLink
    
    def __str__(self):
        """Creates a string representation of the link"""
        tempPrev = self.prev
        tempNext = self.next
        output = f"Link[prevValue: {tempPrev.getValue()} | linkValue: {self.value} | nextValue: {tempNext.getValue()}]"
        return output
    
    def getValue(self):
        """Returns the value for the specified item"""
        return self.value

    def getNext(self):
        """Returns the location of the next link"""
        return self.next

    def getPrev(self):
        """Returns the location of the previous link"""
        return self.prev

    def setNext(self, next):
        """Sets the location of the next link"""
        self.next = next
    
    def clearNext(self):
        """Sets the location of the previous link"""
        self.next = None

    def setPrev(self, prev):
        """Sets the location of the previous link"""
        self.prev = prev

    def clearPrev(self):
        """Sets the location of the previous link"""
        self.prev = None




        

class TextClass:
    def __init__(self):
        """Creates an empty list of links"""
        self.head = None
        self.tail = None
        self.lastFind = None

    def addHead(self, value):
        """Add a new link containing value at the head of the list"""
        if self.head == None: #List is empty if head is null, add item as the head and tail
            self.head = self.tail = TextLink(value)
            
        else: #List is not empty, add item to the head
            temp = TextLink(value, self.head, None)
            self.head.setPrev(temp)
            self.head = temp


    def addTail(self, value):
        """Add a new link containing value at the tail of the list"""
        if self.tail == None: #List is empty if tail is null, add item as the head and tail
            self.head = self.tail = TextLink(value)
        else:
            temp = TextLink(value, None, self.tail)
            self.tail.setNext(temp)
            self.tail = temp
    
    def getHead(self):
        """Return the value from the head of the list (throw an exception if list is empty)"""
        if self.head == None:
            raise ValueError
        else:
            return self.head.getValue()

    def getTail(self):
        """Return the value from the tail of the list (throw and exception if the list is empty)"""
        if self.tail == None:
            raise ValueError
        else:
            return self.tail.getValue()

    def removeHead(self):
        """Removes the value at the head of the list"""
        if self.head == None:
            raise ValueError
        else:
            self.head = self.head.getNext()
            #self.tail.setNext(None)
            if self.head == None:
                self.tail = None
            else:
                self.head.setPrev(None)


    def removeTail(self):
        """Removes the value at the head of the list"""
        if self.tail == None:
            raise ValueError
        else:
            self.tail = self.tail.getPrev()
            #self.tail.setNext(None)
            if self.tail == None:
                self.head = None
            else:
                self.tail.setNext(None)
            
    def find(self, value):
        """Returns true if value is present in the list, returns false if not"""
        valueFound = False
        linkCheck = self.head
        while linkCheck != None and valueFound == False:
            if linkCheck.getValue() == value:
                valueFound = True
            else:
                linkCheck = linkCheck.getNext()
        return valueFound
    
    def findRemove(self, value):
        """Returns true and removes the value if present, returns false if not."""
        valueFound = False
        linkCheck = self.head
        while linkCheck != None and valueFound == False:
            if linkCheck.getValue() == value:
                valueFound = True
                if linkCheck == self.head: #If value found was at the head, call removeHead()
                    self.removeHead()
                elif linkCheck == self.tail: #If value found was at the head, call removeTail()
                    self.removeTail()
                else: #Otherwise, remove link and adjust prev and next links to point to eachother
                    prevLink = linkCheck.getPrev()
                    nextLink = linkCheck.getNext()
                    prevLink.setNext(nextLink)
                    nextLink.setPrev(prevLink)
            else:
                linkCheck = linkCheck.getNext()
        return valueFound
            
    def displayList(self):
        """Returns a string containing the contents of the list from head to tail, should insert a space between each value."""
        currentLink = self.head
        linkEnded = False
        listString = ""
        while linkEnded == False:    
            listString += str(currentLink.getValue()) + " "
            if currentLink.getNext() == None:
                linkEnded = True
            else:
                currentLink = currentLink.getNext()
        return listString

    def append(self, otherList):
        """Append the contents of otherList to the tail of this list."""
        """Version 1: Merges the lists into one, but updates to items that were previously between head and tail of otherList will be updated within otherList"""
        # appendlist = otherList
        # tempHead = appendlist.head
        # newTail = appendlist.tail
        # tempHead.setPrev(self.tail)
        # self.tail.setNext(tempHead)
        # self.tail = newTail
        """Version 2: Cycles from head to tail of otherlist and adds the values found within each link to the tail of the main list. Makes no change to the original strucutre of otherList"""
        appendLink = otherList.head
        while appendLink != None:
            self.addTail(appendLink.getValue())
            appendLink = appendLink.getNext()
            
        
    def findNext(self, value):
        """Like find, but if findNext is called for the same value after a success, it should find the next instance of that value, wrapping if necessary."""
        valueFound = False
        findWrap = False
        if self.lastFind == None or self.lastFind.getNext() == None: #Check if the lastFind has been populated yet as starting point, otherwise use head.
            linkCheck = self.head
        else:
            linkCheck = self.lastFind.getNext()
        while linkCheck != None and valueFound == False:
            if linkCheck.getValue() == value:
                valueFound = True
                self.lastFind = linkCheck
            else:
                linkCheck = linkCheck.getNext()
                if linkCheck == None and findWrap == False: #If we havne't wrapped yet and are now at the end, start again at the head
                    linkCheck = self.head
                    findWrap = True
        return valueFound
        
    def removeLast(self):
        """Removes the link that was saved by the last call to findNext."""
        if self.lastFind != None:
            if self.lastFind == self.head: #If value found was at the head, call removeHead()
                self.removeHead()
            elif self.lastFind == self.tail: #If value found was at the head, call removeTail()
                self.removeTail()
            else: #Otherwise, remove link and adjust prev and next links to point to eachother
                prevLink = self.lastFind.getPrev()
                nextLink = self.lastFind.getNext()
                prevLink.setNext(nextLink)
                nextLink.setPrev(prevLink)    
            self.lastFind = None
    
    def insertLast(self, value):
        """Insert value before the link that was saved by the most recent call to findNext."""
        if self.lastFind != None:
            if self.lastFind == self.head: #If value found was at the head, new value becomes the head
                self.addHead(value)
            else: #Otherwise, remove link and adjust prev and next links to point to eachother
                prevLink = self.lastFind.getPrev()
                temp = TextLink(value, self.lastFind, prevLink)
                prevLink.setNext(temp)
                self.lastFind.setPrev(temp)