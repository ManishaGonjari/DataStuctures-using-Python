# This code includes 2 classes
# One class is responsible to perform operations at node level
# and another class is responsible to perform operations at linked list level

class Node(object):
    def __init__(self,d,r= None):
        self.data = d
        self.next_node = r

    def get_next(self):
         return self.next_node

    def set_next(self,n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self,d):
         self.data = d

    def has_next(self):
        if (self.get_next() is None):
            return False
        else:
            return True

    def to_string(self):
        return str(self.data)


class linkedList(object):
    def __init__(self,r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d):
        new_node = Node (d,self.root)
        self.root = new_node
        self.size += 1


    def remove(self,d):
        this_node = self.root
        prev_node = None

        while(this_node):
            if(this_node.data == d and prev_node ==None):
                self.root = this_node.next_data
                self.size -= 1
                return True
            elif(this_node.data == d):
                prev_node.next_node = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False


    def find(self,d):
        this_node = self.root
        while(this_node):
            if(this_node.data == d):
                return True
            else:
                this_node = this_node.next_node

        return False

    def printlist(self):
        if(self.root is None):
            print "Empty list"
            return False

        this_node = self.root
        while(this_node.has_next()):
            this_node= this_node.get_next()
            print (this_node.to_string())


def main():
    mylist =  linkedList()
    mylist.add(2)
    mylist.add(4)
    mylist.add(6)
    print (mylist.get_size())
    mylist.remove(4)
    print (mylist.get_size())
    mylist.printlist()

main()
