from GeeksLL import LinkedLista
import os
os.system('cls')

class  Task:
    def  __init__(self,  name):
        self.name  =  name  # Task description (string)
        self.complete  =  "incomplete" # Status: "complete" or "incomplete"
        
# You'll need to include your LinkedList and Node classes from the lesson
class  ToDoList:
    def  __init__(self,  list_name="My Tasks"):
        self.list_name  =  list_name
        self.tasks  =  LinkedLista() # Use your LinkedList to store Task objects

    # IMPLEMENT THESE METHODS:
    def  add_task(self,  task_name):
        self.tasks.insertAtBegin(task_name)

    def  complete_task(self,  position):
        """
        Mark a task as complete by position
        Args:
            position (int): Position of the task to mark complete (1-indexed)
        Returns:
            bool: True if task was found and marked complete, False otherwise
        Example:
            Success = todo.complete_task(1)  # Complete first task
            if success:
                print("Task completed!")
        """
        # self.tasks.get_at_position().complete
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
        pass
 
#test stuff here
 
 
        
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