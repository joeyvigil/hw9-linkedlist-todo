Build a To-Do List Manager
--------------------------


### Assignment Overview

Now that you've learned the fundamentals of linked lists and practiced with basic operations and music playlists, it's time to apply these concepts independently. Your task is to create a To-Do List Manager that uses a linked list to store and manage tasks.

This assignment will reinforce your understanding of:

-   Linked list traversal and manipulation

-   Object-oriented programming with custom classes

-   Method implementation and error handling

-   Real-world application of data structures

* * * * *

Project Requirements
--------------------

### Task Class Specification

Create a Task class that represents individual to-do items:
```python
class  Task:
    def  __init__(self,  name):
        self.name  =  name  # Task description (string)
        self.complete  =  "incomplete" # Status: "complete" or "incomplete"
```
### ToDoList Class Specification

Create a ToDoList class that uses your LinkedList from class: https://github.com/dkatina/advanced-python-l2.git

* * * * *

Implementation Guidelines
-------------------------

### Required Methods Implementation

1.  add_task:

-   Create a new Task object

-   Add it to the linked list using the append method

-   Provide user feedback

3.  complete_task:

-   Convert 1-based position to 0-based index

-   Use get_at_position to retrieve the task

-   Set the task's complete attribute to "complete"

-   Return True if successful, False if position is invalid

5.  remove_task:

-   Convert 1-based position to 0-based index

-   Use the linked list's delete_at_position method

-   Return True if successful, False if position is invalid

7.  view_all_tasks:

-   Traverse the linked list and display each task

-   Show task numbers (1-indexed for user friendliness)

-   Use the Task's __str__ method for formatting

### BONUS Methods

1.  view_incomplete_tasks:

-   Similar to view_all_tasks but filter for incomplete tasks only

-   Maintain proper numbering for incomplete tasks

3.  get_task_count:

-   Return the size of the linked list

5.  get_completion_stats:

-   Traverse the linked list and count complete vs incomplete tasks

-   Return the percent of complete tasks

* * * * *

Testing Your Implementation
---------------------------

Use this test function to verify your to-do list works correctly:
```python
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
# test_todo_list()
```
* * * * *

Success Criteria
----------------

Your homework will be evaluated on the following criteria:

-   Task creation: Tasks are properly created with name and completion status

-   Adding tasks: add_task correctly adds tasks to the linked list

-   Completing tasks: complete_task marks tasks complete by position

-   Removing tasks: remove_task removes tasks by position

-   Viewing tasks: view_all_tasks displays all tasks with proper formatting

-   Position validation: Methods handle invalid positions appropriately

Starter Code:
```python
# You'll need to include your LinkedList and Node classes from the lesson
class  ToDoList:
    def  __init__(self,  list_name="My Tasks"):
        self.list_name  =  list_name
        self.tasks  =  LinkedList() # Use your LinkedList to store Task objects

    # IMPLEMENT THESE METHODS:
    def  add_task(self,  task_name):
        """
        Add a new task to the end of the to-do list
        Args:
            task_name (str): Description of the task to add
        Example:
            todo.add_task("Buy groceries")
            todo.add_task("Finish homework")
        """
        # TODO: Implement this method
        pass

    def  complete_task(self,  position):
        """
        Mark a task as complete by position
        Args:
            position (int): Position of the task to mark complete (1-indexed)
        Returns:
            bool: True if task was found and marked complete, False otherwise
        Example:
            Success = todo.complete_task(1)  # Complete first task
            if success:
                print("Task completed!")
        """
        # TODO: Implement this method
        pass

    def  remove_task(self,  position):
        """
        Remove a task from the list by position
        Args:
            position (int): Position of the task to remove (1-indexed)
        Returns:
            bool: True if task was found and removed, False otherwise
        Example:
            success = todo.remove_task(2)  # Remove second task
            if success:
                print("Task removed!")
        """
        # TODO: Implement this method
        pass

    def  view_all_tasks(self):
        """
        Display all tasks in the to-do list with their completion status
        Example output:
            My Tasks
            ========
            1. Buy groceries - Complete
            2. Finish homework -Incomplete
            3. Call dentist - Incomplete
        """
        # TODO: Implement this method
        pass
```
