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
    def __init__(self, value, nextLink="", prevLink=""):
        """Creates a double-pointed link with null pointers if not specified"""
        self.value = value
        self.next = nextLink
        self.prev = prevLink
    
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

    def setPrev(self, prev):
        """Sets the location of the previous link"""
        self.prev= prev




        

class TextClass:
    def __init__(self):
        """Creates an empty list of links"""
        self.head = ""
        self.tail = ""

    def addHead(self, value):
        """Add a new link containing value at the head of the list"""
        if self.head == "": #List is empty if head is null, add item as the head and tail
            self.head = self.tail = TextLink(value)
            
        else: #List is not empty, add item to the head
            temp = TextLink(value, self.head, "")
            self.head.setPrev(temp)
            self.head = temp


    def addTail(self, value):
        """Add a new link containing value at the tail of the list"""
        if self.tail == "": #List is empty if tail is null, add item as the head and tail
            self.head = self.tail = TextLink(value)
        else:
            temp = TextLink(value, "", self.tail)
            self.tail.setNext(temp)
            self.tail = temp
    
    def getHead(self):
        """Return the value from the head of the list (throw an exception if list is empty)"""
        if self.head == "":
            raise ValueError
        else:
            return self.head.getValue()

    def getTail(self):
        """Return the value from the tail of the list (throw and exception if the list is empty)"""
        if self.tail == "":
            raise ValueError
        else:
            return self.tail.getValue()

    def removeHead(self):
        """Removes the value at the head of the list"""
        if self.head == "":
            raise ValueError
        else:
            self.head = self.head.getNext()

    def removeTail(self):
        """Removes the value at the head of the list"""
        if self.tail == "":
            raise ValueError
        else:
            self.tail = self.tail.getPrev()
    
    def find(self, value):
        """Returns true if value is present in the list, returns false if not"""
        valueFound = False
        linkCheck = self.head
        while linkCheck != "" and valueFound == False:
            if linkCheck.getValue() == value:
                valueFound = True
            else:
                linkCheck = linkCheck.getNext()
        return valueFound
    
    def findRemove(self, value):
        """Returns true and removes the value if present, returns false if not."""
        valueFound = False
        linkCheck = self.head
        while linkCheck != "" and valueFound == False:
            if linkCheck.getValue() == value:
                valueFound = True
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
            if currentLink.getNext() == "":
                linkEnded = True
            else:
                currentLink = currentLink.getNext()
        return listString
            
