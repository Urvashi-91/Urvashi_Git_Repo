'''
Source: https://yumminhuang.github.io/note/sreinterview/
Assume there is a REST API available at http://www.employee.com/api for accessing employee information The employee information endpoint is /employee/<id> Each employee record you retrieve will be a JSON object with the following keys:

name refers to a String that contains the employee’s first and last name
title refers to a String that contains the employee’s job title
reports refers to an Array of Strings containing the IDs of the employee’s direct reports
Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.
For example, suppose that Flynn Mackie’s employee id is ‘A123456789’ and his only direct reports are Wesley Thomas and Nina Chiswick.
If you provide ‘A123456789’ as input to your function, you will see the sample output below.
'''
r = requests.get('http://www.employee.com/api/employee/<id>', auth=('user', 'pass'))
r.json()
json.loads()


def foo(id, depth=0):
    ...
    if depth == 0:
        # print without indentation
    else:
        # print with a prefix ' ' * 2 * depth
    ...
    foo(employee, depth + 1)