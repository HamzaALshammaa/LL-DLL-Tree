# بلوك جين
# single linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        print("the list is: ", end=" ")

        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def EvenAndOdd(self):
        cur_node = self.head
        even = 0
        odd = 0
        while cur_node:
            if cur_node.data % 2 == 0:
                even += 1
            else:
                odd += 1
            cur_node = cur_node.next
        print("the a amount of even numbers: ", even)
        print("the a amount of odd numbers: ", odd)

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
                    print("the element is not in the list")
                    return
        else:
            self.head = None

    def reverse(self):
        def reverse(cur, prev):
            if not cur:
                return prev

            neext = cur.next
            cur.next = prev
            prev = cur
            cur = neext
            return reverse(cur, prev)

        self.head = reverse(cur=self.head, prev=None)

    def merge(self, l):
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = l.head
                break
            temp = temp.next


llist = LinkedList()
llist2 = LinkedList()
# llist3 = LinkedList()
# size = int(input("enter the size: "))
# for nums in range(size):
#     llist.insert = int(input("enter a number for list1: "))
# for nums in range(size):
#     llist2.insert = int(input("enter a number: "))
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(7)
llist2.insert(8)
llist2.insert(9)
llist2.insert(10)
llist2.insert(11)
# llist.search(0)
print("the list before the events: ")
llist.print_list()
# print(" ")
# llist.delete_node(5)
# llist.EvenAndOdd()
# llist.print_list()
# llist.reverse()
print(" ")
# llist.print_list()
llist.merge(llist2)
print(llist)
