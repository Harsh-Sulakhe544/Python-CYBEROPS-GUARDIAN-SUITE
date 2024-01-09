# this is a testing file - not working for 3(tasks error unbounded ) and 4(pass tasks for both of them) options 
import json
import logging
import os
import getpass # to lock the keyboard 
# import first  # cuz i want that keyboard-lock facility ==> not possible to point backward 

class Task:
    # create a constructor , by default nothing is completed 
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
        
# why 'yield' below  ->  it is a generator (meaning doesn't occupy large space for data)
# it helps to handle large set of data (instead of returning large set of data(so many tasks get added 
# to list) , it returns each value at a time without taking extra large space  )

def task_generator(tasks):
    for task in tasks:
        yield task

# yield -> also fetch the next-task only when needed (lazy iterator for large data)
def completed_tasks_generator(tasks):
    for task in tasks:
        if task.completed:
            yield task

# use of nested functions , or closure-property , 
# log_operation => is a decorator function, wrapper is a inner function (wrapper is a closure here, 
# cuz it closes over the variable func, so wrapper can access func outside log_operation )

# funcName - function that executes task for log file , filename-> todoapp.py (not main-file)
logging.basicConfig(filename='Debug.log', level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s ')

def log_operation(func):
   # wrapper function can take any number of arguements and keyword args -> *args and **kwargs
    def wrapper(*args, **kwargs):
    # invoke the original function log_operation for chaining of decorators 
        try:
            result = func(*args, **kwargs)
            logging.info(f"Operation: {func.__name__}")
            return result
        except Exception as e:
            logging.error(f"Error in operation {func.__name__}: {str(e)}")
            # Optionally re-raise the exception if needed
            # raise e

    return wrapper

# use decorators , instead of calling the same function , add the task to list and then add task to same 
# log file  by using @log_operation  , 
# pass the original function (add_task) as ARGUEMENT to the (decorator  @log_operation)
@log_operation
def add_task(tasks, title, description=""):
    tasks.append(Task(title, description))

# using decorator , mark the task as completed in log file and tasks.json file
@log_operation
def mark_completed(tasks, title, todo_file):
    # check if task exists or not in tasks.json file using key- title for the dictionary 
    task_exists = any(task.title == title for task in tasks)
    
    if not task_exists:
        print(f"Error: Task with title '{title}' not found.")
        exit()
        
    for task in tasks:
        if task.title == title:
            task.completed = True
            break
        
# display the tasks on console , 
# task_generator_func => calling task_generator => because of yield keyword to fetch each single-task  
def display_tasks(tasks, task_generator_func,  filename):
    # check if we directly hit choice 3 or 4 
    # -> means no json file created only initially (no tasks.json )
    
    if not os.path.exists(filename):
        print("Error: 'tasks.json' file not found. No tasks to display.")
        exit()
        
    tasks = task_generator_func(tasks)
    # if tasks does not exist
    if not tasks:
        print("Error: No tasks found.")
        exit()
        
    # displaying header 
    print("\n TITLE \t DESCRIPTION \t STATUS")
    for task in tasks:
        status = "Completed" if task.completed else "Not Completed"
        print(f"{task.title} \t {task.description} \t\t {status}")

# add tasks to json file tasks.json 
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        # create a list of dictionary for a single task 
        task_list = [{'title': task.title, 'description': task.description, 'completed': task.completed} for task in tasks]
        # convert the list task_list to json format 
        json.dump(task_list, file)


def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            # read the data for a specific task from tasks.json file using json.load()
            task_list = json.load(file)
            
            # list comprehension , we want to laod each dictionary in tasks list from json-file , 
            # Task( task['title'] , task['description'] ) for task in task_list ]
            
            # task is dictionary , collect all Tasks in a list format , 
            # so it is [ {task1} , {task2} ,  {task3} , ... ]
            tasks = [ Task(task['title'] , task['description'] ) for task in task_list ]
            
            # iterate over all tasks using enumerate()  
            for i, task in enumerate(tasks):
                # i is index , task => each task {} , task is completed 
                task.completed = task_list[i]['completed'] 
                
            return tasks
        
        # if there is no tasks , dont parse the json only 
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():
    # todo_file stores all tasks in json format 
    todo_file = 'tasks.json'
    
    # initially add the task in to tasks.json
    tasks = load_tasks(todo_file)

    while True:
        print("\n \n ===== To-Do List Menu ===== \n ")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display All Tasks")
        print("4. Display Completed Tasks")
        print("5. Exit")

        
        # lock for waste inputs , only integer is accepted , and displayed  
        def get_integer_input(prompt):
            while True:
                try:
                    user_input = getpass.getpass(prompt)
                    if user_input: 
                        result = int(user_input)  # Try to convert to integer
                        print(result)
                        return result
                
                except ValueError:
                    print("\n \n Invalid input. Please enter an integer.")
                
                
        choice = None 
        
        while not isinstance(choice, int):
            choice = get_integer_input("Enter your choice: ")

        # dont check for '1' => by default it is string (python will noot check number)
        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(tasks, title, description)
            save_tasks(tasks, todo_file)

        elif choice == 2:
            title = input("Enter the title of the task to mark as completed: ")

            # dont use try-except , will not work here , instead directly pass file 
            mark_completed(tasks, title, todo_file)
            save_tasks(tasks, todo_file)

        elif choice == 3:
            display_tasks(tasks,task_generator, todo_file)

        elif choice == 4:
            display_tasks(tasks, completed_tasks_generator, todo_file)

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please try again.")