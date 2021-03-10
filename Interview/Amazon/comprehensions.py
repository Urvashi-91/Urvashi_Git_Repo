'''
Comprehensions in Python
    - wite a list or dict in comprehension
    - add conditional statements to a comprehension
    - write nested comprehensions
    - replace a map function with a comprehension
    - complete a lab by writing a comprehension

Scenario: Python developer for high security customer, so based in snippets refactor a simpler forms
'''

'''
Substitute a for loop with a list comprehension'''

# Example 1 for loop
float_list = []
for i in range(100):
    float_list.append(i * 100.0)

# Example 1 list comprehension
float_list = [i * 100.0 for i in range(100)]  # value is considered before the for


# Example 2
def old_process_incoming_data(data_list):
    temp = []
    for datum in data_list:
        temp.append(datum // 2 * 67 - 5)
    return temp


# Example 2 comprehension
def process_incoming_data(data_list):
    return [datum // 2 * 67 - 5 for datum in data_list]  # no extra variable needed to store the output


# Testing
if __name__ == "__main__":
    data_list = [0, 5, 10, 15]
    print(process_incoming_data(data_list) == old_process_incoming_data(data_list))

'''
Substitute a Loop with a Dict comprehension
'''

# Example 3 for loop of dict
float_dict = {}
for i in range(10):
    float_dict[i] = i * 100.0

# Example 3 comprehension
float_dict = {i: i * 100.0 for i in range(10)}  # key: value for dict and for list its just value

# Example 4 for dict
hydration_levels = {"arc1": 23, "arc2": 64, "arc3": 104}


def old_saturation_levels(data_dict):
    temp = {}
    for key, value in data_dict.items():
        temp[key] = (value ** 3) / (2 ** value)
    return temp


def saturation_levels(data_dict):
    return {key: (value ** 3) / (2 ** value) for key, value in data_dict.items()}


# Testing
if __name__ == "__main__":
    print(saturation_levels(hydration_levels) == old_saturation_levels(hydration_levels))

'''
Add conditionals to comprehensions
'''

# Example 5 for loop with if-else
float_list = []
for i in range(100):
    if i % 2 == 0:
        float_list.append(i * 100.0)
    else:
        float_list.append(-1)

# Example 5 List comprehension
float_list = [i * 100.0 if i % 2 == 0 else -1 for i in range(100)]


# Example 6 for loop if-else
def old_find_usable_data(data_list):
    temp = []
    for datum in data_list:
        if datum > 90 and datum % 2 == 0:
            temp.append(datum)
        else:
            temp.append(-100)
    return temp


# Example 6 List comprehension
def find_usable_data(data_list):
    return [datum if datum > 90 and datum % 2 == 0 else -100 for datum in data_list]

'''if the condition is changing the data to be printed then it goes before for loop. 
If the conditions are not changing the return value only suggesting if the data should be 
returned or not then it goes after for loop'''


# Test Case
if __name__ == "__main__":
    data_list = [1,2,90,91,92,67]
    print(old_find_usable_data(data_list) == find_usable_data(data_list))

#Example 7 for loop - Nested loop
float_list = []
for i in range(100):
    for j in range(10):
        float_list.append(i * j)

#Example 7 List comprehension for nested loops
float_list = [i*j for i in range(100) for j in range(10)]

#Example 8 nested loop
def old_calculate_value(data_list, divisors_list):
    temp = []
    for datum in data_list:
        for divisor in divisors_list:
            temp.append(datum / divisor)
    return temp

#Example 8 list comprehensions
def calculate_value(data_list, divisors_list):
    return [datum/divisor for datum in data_list for divisor in divisors_list]

#testing
if __name__ == '__main__':
    data_list = [1,2,3,4,5]
    divisors_list = [20,21,22]
    print(old_calculate_value(data_list,divisors_list) == calculate_value(data_list, divisors_list))

'''
Use a Function for the result of a Comprehension: Introducing Map'''

#Example 9 for Maping
numbers = [1.0,2.0,3.0,4.0]
def my_operation(i):
    return i*2
#map function
doubled_list = map(my_operation, numbers)
list (doubled_list)

#Example 9 list comprehension
doubled_list = [my_operation(i) for i in numbers]

#Example 10 Mapping
def old_corrected_value(value):
    return value * 32

#testing
if __name__ == '__main__':
    data_list = [1,2,3]
    old_results = map(old_corrected_value, data_list)
    results = [old_corrected_value(datum) for datum in data_list]
    print(list(old_results) == results)


#Example 10
from math import pi
radius = [1,2,3,4,5]
for r in radius:
    circle_area[r] = pi * r ** 2

circle_area = {r:pi*r**2 for r in radius}