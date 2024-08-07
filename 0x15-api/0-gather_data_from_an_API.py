#!/usr/bin/python3
'''
gather employee data from API
'''

import re
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee data
    user_response = requests.get(f"{url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    employee = user_response.json()
    employee_name = employee['name']
    
    # Fetch TODO list data
    todos_response = requests.get(f"{url}/todos", params={"userId": employee_id})
    todos = todos_response.json()
    
    # Calculate number of done tasks and total tasks
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo['completed']]
    number_of_done_tasks = len(done_tasks)
    
    # Print the results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
