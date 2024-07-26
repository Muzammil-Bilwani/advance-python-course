## Course Content: Introduction to Lambda Functions in Python

### What are Lambda Functions?

Definition and purpose of lambda functions
Comparison with regular functions
Advantages of using lambda functions

### Syntax and Basic Usage

- Syntax:
  `lambda arguments: expression`

#### Differences between lambda functions and traditional functions

#### Basic Lambda Function

```python
# Traditional function
def add(x, y):
    return x + y

print(add(2, 3))  # Output: 5

# Lambda function
add_lambda = lambda x, y: x + y
print(add_lambda(2, 3))  # Output: 5
```

#### Lambda Function with No Arguments

```python
# Lambda function with no arguments
no_arg_lambda = lambda: "Hello, World!"
print(no_arg_lambda())  # Output: Hello, World!
```

### Lambda Functions with map, filter, and reduce

#### Using map with Lambda

```python

# Traditional function
def square(x):
return x \*\* 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

# Using lambda with map

squared_numbers_lambda = list(map(lambda x: x \*\* 2, numbers))
print(squared_numbers_lambda) # Output: [1, 4, 9, 16, 25]
```

### Using filter with Lambda Functions

- Purpose of filter
- Filtering elements in a list based on a condition

#### Using filter with Lambda

```python

# Traditional function

def is_even(x):
return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # Output: [2, 4, 6]

# Using lambda with filter

even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_lambda) # Output: [2, 4, 6]

```

### Using reduce with Lambda Functions

- Purpose of reduce

#### Using reduce with Lambda

```python
from functools import reduce

# Traditional function

def multiply(x, y):
return x \* y

numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
print(product) # Output: 120

# Using lambda with reduce

product_lambda = reduce(lambda x, y: x \* y, numbers)
print(product_lambda) # Output: 120
```

### Combining map, filter, and reduce with Lambda Functions

#### Advanced examples using combinations of map, filter, and reduce - Combining map, filter, and reduce

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map: square each number

squared_numbers = list(map(lambda x: x \*\* 2, numbers))

# Filter: keep only even squares

even_squared_numbers = list(filter(lambda x: x % 2 == 0, squared_numbers))

# Reduce: sum the remaining numbers

sum_even_squared = reduce(lambda x, y: x + y, even_squared_numbers)

print(sum_even_squared) # Output: 220

```

### Class Exercises

#### Exercise 1: Basic Lambda Functions

##### Question: Create a lambda function that multiplies two numbers and returns the result. Use this lambda function to multiply 5 by 7.

#### Exercise 2: Using map with Lambda Functions

##### Question: You have a list of numbers [1, 2, 3, 4, 5]. Use the map function and a lambda function to create a new list where each number is increased by 10.

#### Exercise 3: Combining filter and reduce with Lambda Functions

##### Question: Given a list of numbers [3, 6, 9, 12, 15, 18, 21], use the filter function to select numbers greater than 10. Then, use the reduce function to calculate the sum of the filtered numbers.

#### Solution

##### Exersice 1

```python
multiply = lambda x, y: x * y
result = multiply(5, 7)
print(result)  # Output: 35
```

##### Exercise 2

```python
numbers = [1, 2, 3, 4, 5]
increased_numbers = list(map(lambda x: x + 10, numbers))
print(increased_numbers)  # Output: [11, 12, 13, 14, 15]
```

##### Exercise 3

```python
from functools import reduce

numbers = [3, 6, 9, 12, 15, 18, 21]

# Filter: select numbers greater than 10
filtered_numbers = list(filter(lambda x: x > 10, numbers))

# Reduce: calculate the sum of filtered numbers
sum_filtered = reduce(lambda x, y: x + y, filtered_numbers)

print(sum_filtered)  # Output: 66
```

### Class Quiz

- Question: You have a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. Use the filter function and a lambda function to create a new list that contains only the strings with more than 5 characters.

  - Input: ['apple', 'banana', 'cherry', 'date', 'elderberry']
  - Expected Output: ['banana', 'cherry', 'elderberry']

- Question: Given a list of numbers [2, 4, 6, 8, 10], first use the map function and a lambda function to double each number. Then, use the reduce function to find the product of the doubled numbers.

  - Input: [2, 4, 6, 8, 10]
  - Expected Output: 122880 (Product of [4, 8, 12, 16, 20])
