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




        

class TextList:
    def __init__(self):
        """Creates an empty list of links"""
        self.head = ""
        self.tail = ""

    def addHead(self, value):
        """Add a new link containing value at the head of the list"""
        if self.head == "": #List is empty if head is null, add item as the head and tail
            TextLink(value)
            
        else: #List is not empty, add item to the head
            TextLink(value, "", self.head)


    def addTail(self, value):
        """Add a new link containing value at the tail of the list"""
