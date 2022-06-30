# create a single new node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # print the element of linked list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next

    # insert an element to the linked list
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # make a copy of the head
    def getHead(self):
        return self.head

    def merge2(self, l):
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = l.head
                print("the new list is: ", temp.data)
                break
            temp = temp.next

    # insert element at the first of linked list
    def insertAtFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtMiddle(self, key, data):
        prev_node = self.getHead()
        new_node = Node(data)
        if prev_node.next is None:
            print("hi")
        else:
            while prev_node.next is not None:
                if key is prev_node.data:
                    new_node.next = prev_node.next
                    prev_node.next = new_node

                prev_node = prev_node.next
            print('key was not found')

    # insert element at middle of linked list by give it the previous node
    def insertAtEnd(self, data):
        newNode = Node(data)
        prevNode = self.head
        if self.head is None:
            self.head = newNode
        else:
            while prevNode.next is not None:
                prevNode = prevNode.next
            prevNode.next = newNode

    # delete a node based on given key
    def deleteNode(self, key):
        temp = self.head
        prev = temp
        # If head node hold the key to be deleted
        if temp is not None:
            if temp.data is key:
                self.head = temp.next
                temp = None
                return
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data is key:
                prev.next = temp.next
                temp = None
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            print('key was not found')
            return
        # Unlink the node from linked list

    # check how many even and odd element in the linked list
    def checkData(self):
        evenNumber = 0
        oddNumber = 0
        current = self.head
        while current:
            if current.data % 2 == 0:
                evenNumber = evenNumber + 1
            else:
                oddNumber = oddNumber + 1
            current = current.next

        print('the even number is :', evenNumber)
        print('the odd number is :', oddNumber)

    # search for element if its in liked list
    def search(self, key):
        temp = self.head
        if temp.next is not None:
            if temp.data == key:
                print('the element is in the node ')
            else:
                while temp is not None:
                    if temp.data == key:
                        print('the element is in the node')
                        break

                    temp = temp.next
                if temp is None:
                    print("the element you entered is not in the linked list")
                    return
        else:
            self.head = None

    # merge between tow linked list

    # reverse the linked list
    def reverse(self):
        print("\n")
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
        return self.head

    # git the middle of linked list
    def getmid(self):
        temp = self.head.next
        prev = self.head
        while temp and temp.next:
            temp = temp.next.next
            prev = prev.next
        print('the middle number is : ', prev.data)

    def sortList(self):
        if self.head is None:
            print('list is empty')
        else:
            current = self.head
            while current.next is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    def merge(self, l):
        temp = self.getHead()
        while temp:
            if temp.next is None:
                temp.next = l.getHead()
                break
            temp = temp.next

    def mearge2L(self, l1, l2):
        temp = self.head
        temp2 = l1.head
        temp3 = l2.head
        while temp:
            if l1.next is None:
                if temp2.data < temp3.data:
                    temp.data = temp2.data
                else:
                    temp.data = temp3.data
                break
            temp = temp.next
            # print(temp.data, end=" ")


l3 = LinkedList()
l1 = LinkedList()
l2 = LinkedList()
# l1 = [1, 3, 5, 6]
l1.insert(1)
l1.insert(3)
l1.insert(5)
l1.insert(6)
# l2 = [2, 4, 7, 10]
l2.insert(2)
l2.insert(4)
l2.insert(7)
l2.insert(10)
print("hay 1")
l1.print_list()
print(" hay 2")
l2.print_list()
l3.mearge2L(l1, l2)
print(" hay 3")
l3.print_list()
# size = int(input('enter the size of node : '))
# for i in range(size):
#     l1.insert(int(input('enter the element : ')))
# l1.insert(1)
# l1.insert(2)
# l1.insert(3)
# l2.insert(4)
# l2.insert(5)
# l2.insert(6)
# l2.insert(7)
# size2 = int(input('enter the size of the second node : '))
# for i in range(size2):
#     l2.insert(int(input('enter the element : ')))
# l1.merge2(l2)
# l1.print_list()
# print()
# l1.merge2(l2)
# l1.print_list()
