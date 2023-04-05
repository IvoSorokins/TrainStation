class TrainLinkedList:
    number = 0  # Instead of TrainLinkedList I will use number - as counters name

    def __init__(self):
        self.head = None  # Used for linked list, starts from head,head pointer to keep track of the first node
        self.tail = None  # Used for linked list, points to the last node in the list
        self.number = f"TrainLinkedList-{TrainLinkedList.number}"
        TrainLinkedList.number += 1  # Increments counter by 1

    class Node:  #
        def __init__(self, carriage):
            self.carriage = carriage
            self.next = None  # Linked lists must set pointers for next element in list using "next" keyword

    def add_first(self, carriage):  # Create a new node with the given carriage
        new_node = TrainLinkedList.Node(carriage)
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the head to the new node
            self.tail = new_node  # set the tail to the new node
        else:
            new_node.next = self.head  # Set the new node's "next" pointer to the current head
            self.head = new_node  # Set the head to the new node

    def add_last(self, carriage):
        new_node = TrainLinkedList.Node(carriage)  # Create a new node with given carriage
        if self.tail is None:  # If the list is empty
            self.head = new_node  # Set the head to the new node
            self.tail = new_node  # Set the tail to the new node
        else:
            self.tail.next = new_node  # Set the current tail's "next" pointer to the new node
            self.tail = new_node  # Set the tail to the new node

    def add_after(self, new_carriage, after_carriage):
        new_node = TrainLinkedList.Node(new_carriage)  # Create a new node with the given new carriage
        current_node = self.head  # Start at the head of the list
        while current_node is not None:
            if current_node.carriage == after_carriage:  # If the current node's carriage matches the after carriage

                # Set the new node's "next" pointer to the current node's "next" pointer
                new_node.next = current_node.next

                current_node.next = new_node  # Set the current node's "next" pointer to the new node
                if current_node == self.tail:  # If the current node is the tail
                    self.tail = new_node  # Set the tail to the new node
                return
            current_node = current_node.next  # Move on to the next node
            raise ValueError(
                # If the after carriage is not found, raise an error
                f"{after_carriage} is not found in the linked list")

    def add_before(self, new_carriage, before_carriage):
        # Create a new node with given carriage
        new_node = TrainLinkedList.Node(new_carriage)

        # If the list is empty, raise an error
        if self.head is None:
            raise ValueError("Linked list is empty.")

        # If the before carriage matches the head node's carriage, insert the new node at the head
        elif self.head.carriage == before_carriage:
            new_node.next = self.head
            self.head = new_node
            return

        # Otherwise, traverse the list and insert the new node before the node with the before carriage
        else:
            prev_node = None
            current_node = self.head
            while current_node is not None:
                if current_node.carriage == before_carriage:
                    # Set the new node's "next" pointer to the current node
                    new_node.next = current_node
                    # Set the previous node's "next" pointer to the new node
                    prev_node.next = new_node
                    return
                prev_node = current_node
                current_node = current_node.next
                # If the before carriage is not found in the list, raise an error
            raise ValueError(f"{before_carriage} is not found in the linked list.")

    def remove_carriage(self, carriage):
        if self.head is None:
            raise ValueError("Linked list is empty")
        elif self.head.carriage == carriage:
            self.head = self.head.next
            if self.head is None:  # If the list becomes empty - Error checking
                self.tail = None
            return
        else:
            prev_node = None
            current_node = self.head
            while current_node is not None:
                if current_node.carriage == carriage:
                    prev_node.next = current_node.next
                    if current_node == self.tail:  # If the removed node is the tail
                        self.tail = prev_node
                    return
                prev_node = current_node
                current_node = current_node.next
            raise ValueError(f"{carriage} is not found in the linked list")

    def remove_carriage_by_position(self, position):
        # Check if the linked list is empty
        if self.head is None:
            raise ValueError("Linked list is empty.")
        # If position is 0, remove the head node
        elif position == 0:
            self.head = self.head.next
            # Check if the linked list is now empty
            if self.head is None:
                self.tail = None
            return
        else:
            current_node = self.head
            prev_node = None
            current_position = 0
            # Traverse the linked list to find the node at the given position
            while current_node is not None:
                if current_position == position:
                    # Remove the node by updating the previous node's next pointer
                    prev_node.next = current_node.next
                    # Check if the removed node was the tail node
                    if current_node.next is None:
                        self.tail = prev_node
                    return
                prev_node = current_node
                current_node = current_node.next
                current_position += 1
            # If position is greater than the length of the linked list, raise an error
            raise ValueError(f"Position {position} is not found in the linked list.")
