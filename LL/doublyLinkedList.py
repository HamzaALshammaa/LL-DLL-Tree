class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly:
    def __init__(self):
        self.head = None

    def insert_element(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("The list is empty")

    def insert_to_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        new = self.head
        # Iterate till the next reaches NULL
        while new.next is not None:
            new = new.next
        new_node = Node(data)
        new.next = new_node
        new_node.prev = new

    def delete_at_start(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None
            if self.head is not None:
                self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("Can't delete elements, the list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        new = self.head
        while new.next is not None:
            new = new.next
        new.prev.next = None

    def display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            temp = self.head
            print("Element is: ")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
        print("\n")

    # def specific(self):
    #     temp1 = self.head
    #     temp = None
    #     while temp1.next is not None:

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

    def delete_specific(self, key):
        current = self.head
        if self.head is not None:
            if self.head.data is key:
                self.delete_at_start()  # use the delete first node function
            else:
                while current.next is not None:
                    if current.data is key:
                        break
                    current = current.next
                if current.next:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    current = None
                else:
                    if current.data is key:
                        self.delete_at_end()  # use the delete last node function
                    else:
                        print('the key you enter is not in the linked list')
        else:
            print('you are deleting from empty linked list')

    def delete_specific_and_next(self, key):
        current = self.head
        if self.head is not None:
            if self.head.data is key:
                if self.head is not None:
                    temp = self.head
                    self.head = self.head.next.next
                    temp = None
                    if self.head is not None:
                        self.head.prev = None
            else:
                while current.next is not None:
                    if current.data is key:
                        break
                    current = current.next
                if current.next:
                    current.prev.next = current.next.next
                    current.next.next.prev = current.prev
                    current = None
                else:
                    if current.data is key:
                        self.delete_at_end()  # use the delete last node function
                    else:
                        print('the key you enter is not in the linked list')
        else:
            print('you are deleting from empty linked list')


doubly = Doubly()
number_of_elements = int(input("enter the number of elements: "))
num = int(input("Enter an element: "))
doubly.insert_element(num)
for nums in range(number_of_elements-1):
    element = int(input(""))
    doubly.insert_to_end(element)

doubly.display()
doubly.delete_at_start()
doubly.display()
# doubly.delete_at_end()
# doubly.display()
doubly.delete_at_start()
doubly.display()
doubly.delete_specific(3)
doubly.display()
doubly.delete_specific(4)
doubly.display()
doubly.delete_specific(5)
doubly.display()
doubly.delete_specific(6)
doubly.display()
# doubly.reverse()
# doubly.display()
# delete = int(input("enter the disierd elemeint to delete: "))
doubly.delete_specific_and_next(7)
doubly.display()
