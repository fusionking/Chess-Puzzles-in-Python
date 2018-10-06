from __future__ import print_function
import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        current = self.head
        if self.head is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node
   
    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total
  
    def display(self):
        elems = []
        current = self.head
        while current is not None:
            elems.append(current.data)
            current = current.next
        print(elems)

    def get(self, key):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == key:
                return cur_node.data
            cur_node = cur_node.next
        return None
    
    def erase(self, key):
        if not self.get(key):
            print("The key {} is not found".format(key))

        cur_node = self.head

        if cur_node is not None:
            if cur_node.data == key:
                self.head = cur_node.next
                cur_node = None
                return

        while cur_node is not None:
            if cur_node.data == key:
                break
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None


def remove_duplicates(head):
    """removes duplicate keys in a linked list, preserving the order"""
    copy_head = second_head = head
    while copy_head is not None:
        while second_head.next is not None:
            if second_head.next.data == copy_head.data:
                second_head.next = second_head.next.next
            else:
                second_head = second_head.next
        copy_head = second_head = copy_head.next


def find_greater(head, x):
    """returns list of unique keys that are greater than number x"""
    keys = []
    current = head
    while current is not None:
        if current.data > x:
            keys.append(current.data)
        current = current.next
    return keys


def remove_greater(l, x):
    """removes keys greater than number x"""
    remove_duplicates(l.head)
    head = l.head
    keys = find_greater(head, x)
    for key in keys:
        l.erase(key)


if __name__ == '__main__':
    number = int(input("Enter maximum number: "))
    min_range, max_range = map(lambda elt: int(elt), 
        input("Enter minimum and maximum range for the linked list: ").split())
    length = int(input("Enter the length of the linked list: "))
    my_list = LinkedList()
    data_list = [random.randint(min_range,max_range) for _ in range(length)]
    for i in data_list:
        my_list.append(i)
    my_list.display()
    remove_greater(my_list, number)
    my_list.display()