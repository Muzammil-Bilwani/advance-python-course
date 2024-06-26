# Advanced Python Course

## Variables and Data Types

### Variables

Variables are used to store data in a program. In Python, you don't need to declare the type of variable explicitly.

```python
# Example of variable assignment
x = 10
y = 3.14
name = "Alice"
is_student = True
```

### Data Types

Python has several built-in data types, including integers, floats, strings, and booleans.

```python
# Integer
age = 20

# Float
height = 5.9

# String
greeting = "Hello, World!"

# Boolean
is_python_fun = True
```

## Operators and Expressions

### Arithmetic Operators

### Arithmetic operators are used to perform mathematical operations.

```python
a = 10
b = 3

addition = a + b      # 13
subtraction = a - b   # 7
multiplication = a * b # 30
division = a / b      # 3.333...
modulus = a % b       # 1
exponentiation = a ** b # 1000
floor_division = a // b # 3

```

## Comparison Operators

Comparison operators compare two values and return a boolean.

```python

x = 5
y = 10

is_equal = (x == y)       # False
is_not_equal = (x != y)   # True
is_greater = (x > y)      # False
is_less = (x < y)         # True
is_greater_equal = (x >= y) # False
is_less_equal = (x <= y)  # True

```

## Logical Operators

Logical operators combine boolean expressions.

```python
a = True
b = False

and_operator = a and b    # False
or_operator = a or b      # True
not_operator = not a      # False
```

## Control Flow (if-else, loops)

### If-Else Statements

The `if` statement is used for conditional execution of code.

````python
# Example of if-else statement
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
    ```
````

### Elif Statements

You can chain multiple conditions using elif.

```python
# Example of if-elif-else statement
x = 10

if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is less than or equal to 5")

```

## Loops

### For Loops

A for loop is used for iterating over a sequence.

```python
# Example of a for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### While Loops

A while loop is used to execute a block of code repeatedly as long as a condition is true.

```python
# Example of a while loop
i = 1

while i < 6:
    print(i)
    i += 1
```

## Functions and Modules

### Functions

A function is a block of code that only runs when it is called.

```python
# Example of a function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

```

### Modules

A module is a file containing Python code. A module can define functions, classes, and variables.

```python

# Example of importing a module
import math

print(math.pi)

```

## Lists, Tuples, Dictionaries

### Lists

A list is a collection of items in a particular order.

```python

# Example of a list
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry

# 2nd Example of a list
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])  # Output: 1

# Modifying elements
numbers[0] = 10
print(numbers)  # Output: [10, 2, 3, 4, 5]

```

### Tuples

A tuple is an immutable collection of items.

```python

# Example of a tuple

fruits = ("apple", "banana", "cherry")

print(fruits[0])  # apple
print(fruits[1])  # banana

```

### Dictionaries

A dictionary is a collection of key-value pairs.

```python

# Example of a dictionary

person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

print(person["name"])  # Alice

```

#### Common Confusions

Difference between Lists and Tuples:

- Lists are mutable, while tuples are immutable.
- Lists use square brackets `[]`, while tuples use parentheses `()`.
- Lists are used for homogenous elements, while tuples are used for heterogeneous elements.

## Interview Questions

### Questions

#### Variables and Data Types

- What is the difference between mutable and immutable data types? Provide examples.
- How would you convert a string to an integer in Python?
- Explain the difference between None, 0, and "" in Python.

#### Operators and Expressions

- What is the difference between == and is operators in Python?
- How do you perform floor division in Python? Provide an example.
- What will be the result of the expression 2 ** 3 ** 2 and why?

#### Control Flow (if-else, loops)

- How would you use a for loop to iterate over a dictionary in Python?
- What is the difference between break, continue, and pass statements in loops?

#### Functions and Modules

- How do you define a function with default parameters in Python?
- Explain how you would import a specific function from a module in Python.

#### Lists, Tuples, Dictionaries

- How do you add an element to a specific position in a list?
- Explain how you can sort a list of tuples based on the second element.

## Answers

### Variables and Data Types

- What is the difference between mutable and immutable data types? Provide examples.

  - Mutable data types can be changed after their creation, whereas immutable data types cannot. Examples:

        - Mutable: list, dict, set
        - Immutable: int, float, str, tuple

- How would you convert a string to an integer in Python?

```python
    s = "123"
    num = int(s)
    print(num) # Output: 123
```

- Explain the difference between None, 0, and "" in Python.

  - None is a special constant in Python that represents the absence of a value or a null value.
  - 0 is an integer value representing zero.
  - "" is an empty string, which is a sequence of characters of length zero.

### Operators and Expressions

- What is the difference between == and is operators in Python?

  - == checks for value equality, i.e., whether the values of two objects are equal.
  - is checks for reference equality, i.e., whether two references point to the same object in memory.

- How do you perform floor division in Python? Provide an example.

  - Floor division can be performed using the // operator.

```python
result = 7 // 3
print(result) # Output: 2
```

- What will be the result of the expression 2 ** 3 ** 2 and why?

  - The expression 2 ** 3 ** 2 is evaluated as 2 ** (3 ** 2), which is 2 \*\* 9 = 512.

```python
result = 2 ** 3 ** 2
print(result) # Output: 512
```

Control Flow (if-else, loops)
How would you use a for loop to iterate over a dictionary in Python?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterating over keys
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
```

- What is the difference between break, continue, and pass statements in loops?

  - break: Exits the loop immediately.
  - continue: Skips the current iteration and moves to the next iteration.
  - pass: Does nothing; it acts as a placeholder.

```python
    for i in range(5):
        if i == 2:
            break  # Loop stops when i is 2
        print(i)

    for i in range(5):
        if i == 2:
            continue  # Skip the rest of the code inside the loop for this iteration
        print(i)

    for i in range(5):
        if i == 2:
            pass  # Do nothing
        print(i)

```

### Functions and Modules

- How do you define a function with default parameters in Python?

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
```

- Explain how you would import a specific function from a module in Python.

```python
# Assuming mymodule.py contains a function called add
# mymodule.py
def add(a, b):
    return a + b

# main.py

from mymodule import add

result = add(5, 3)
print(result) # Output: 8

```

## Lists, Tuples, Dictionaries

- How do you add an element to a specific position in a list?

```python
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)  # Insert 3 at index 2
print(numbers)  # Output: [1, 2, 3, 4, 5]

```

- Explain how you can sort a list of tuples based on the second element.

```python
# List of tuples
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]

# Sort based on the second element (age)
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

```
