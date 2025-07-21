class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class Linked_List:
    def __init__(self):
        self.head = None
    
    # Method to add a node at the beginning of the LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        # print(f"added {new_node}")

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Update node at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return

        # If there's only one node
        if self.head.next is None:
            self.head = None
            return

        # Traverse to the second last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    # Method to remove a node at a given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    # Method to remove a node from the linked list by its data
    def remove_node(self, data):
        current_node = self.head

        # If the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        # Traverse and find the node with the matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If the data was not found
        print("Node with the given data not found")

    # Print the size of the linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def getAtIndex(self, index):
        node = self.head
        count = 0
        while count != (index):
            node = node.next
            count += 1
        return node
    
class  Task:
    def  __init__(self,  name):
        self.name  =  name  # Task description (string)
        self.complete  =  "incomplete" # Status: "complete" or "incomplete"
        
# You'll need to include your LinkedList and Node classes from the lesson
class  ToDoList:
    def  __init__(self,  list_name="My Tasks"):
        self.list_name  =  list_name
        self.tasks  =  Linked_List() # Use your LinkedList to store Task objects

    # IMPLEMENT THESE METHODS:
    def  add_task(self,  task_name):
        self.tasks.insertAtBegin(Task(task_name))

    def  complete_task(self,  position):
        # self.tasks.getAtIndex(position).complete = "complete"
        pass

    def  remove_task(self,  position):
        """
        Remove a task from the list by position
        Args:
            position (int): Position of the task to remove (1-indexed)
        Returns:
            bool: True if task was found and removed, False otherwise
        Example:
            success = todo.remove_task(2)  # Remove second task
            if success:
                print("Task removed!")
        """
        # TODO: Implement this method
        pass

    def  view_all_tasks(self):
#         My Tasks
#             ========
#             1. Buy groceries - Complete
        print("---------- My Tasks ----------")
        print("==============================")
        count =0
        while self.tasks.getAtIndex(count):
            print(f"{count+1}. {self.tasks.getAtIndex(count).data.name} - {self.tasks.getAtIndex(count).data.complete}")
            count +=1
        # self.tasks.printLL()
 
 
 
def  test_todo_list():
    """Test function to verify ToDoList functionality"""
    print("=== Testing To-Do List Implementation ===\n")
    
    # Create a new to-do list
    todo  =  ToDoList("School Tasks")
    
    # Test adding tasks
    print("1. Adding tasks...")
    todo.add_task("Study for math exam")
    todo.add_task("Write history essay")
    todo.add_task("Submit science project")
    todo.add_task("Read chapter 5")
    
    # Test viewing all tasks
    print("\n2. Viewing all tasks:")
    todo.view_all_tasks()
    
    # Test completing tasks
    print("\n3. Completing some tasks...")
    todo.complete_task(2) # Complete second task
    todo.complete_task(4) # Complete fourth task
    
    # Test viewing after completion
    print("\n4. Viewing tasks after completion:")
    todo.view_all_tasks()
    
    # Test removing tasks
    print("\n5. Removing a task...")
    todo.remove_task(3) # Remove third task
    todo.view_all_tasks()
    
    # Test edge cases
    print("\n6. Testing edge cases...")
    print("Trying to complete task at invalid position:")
    result  =  todo.complete_task(10) # Position that doesn't exist
    print(f"Result: {result}")
    print("Trying to remove task at invalid position:")
    result  =  todo.remove_task(0) # Invalid position (should be 1-indexed)
    print(f"Result: {result}")
    print("\n=== Test completed! ===")
    
# Run the test
test_todo_list()