# Week 11: Introduction to Python and Multithreading

- Introduction to multithreading
- Basics of threading module
- Thread synchronization and locks
- Practical exercises and assignments

#### What is process and thread?

- **Process**: A process is an instance of a program that is being executed. It contains the program code, data, and resources of the program being executed. Each process has its own memory space and resources, and runs independently of other processes.

- **Thread**: A thread is a lightweight process that can be managed by the operating system. Threads share the same memory space and resources of the process that created them. Multiple threads can run concurrently within a single process, allowing for parallel execution of tasks.

#### Why use threads?

- **Concurrency**: Threads allow multiple tasks to be executed concurrently within a single process. This can improve the performance and responsiveness of applications by utilizing the available CPU resources more effectively.

- **Parallelism**: Threads can be used to perform multiple tasks in parallel, taking advantage of multi-core processors to speed up the execution of tasks.

- **Asynchronous I/O**: Threads can be used to perform I/O operations asynchronously, allowing the program to continue executing other tasks while waiting for I/O operations to complete.

#### Threading in Python

Python provides a built-in `threading` module that allows you to create and manage threads in your programs. The `threading` module provides a high-level interface for working with threads, making it easy to create and start new threads, synchronize thread execution, and communicate between threads.

#### Creating Threads

To create a new thread in Python, you can define a new class that extends the `Thread` class from the `threading` module, or you can define a function that will be executed by the thread. Here's an example of creating a thread using a function:

```python
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

# Create a new thread

t = threading.Thread(target=print_numbers)

# Start the thread

t.start()
```

In this example, we define a function `print_numbers` that prints numbers from 1 to 5. We then create a new `Thread` object `t` with the target function set to `print_numbers`, and start the thread using the `start` method.

#### Thread Synchronization and Locks

When working with multiple threads, it's important to ensure that shared resources are accessed safely to prevent dead locks.

Python provides a `Lock` class from the `threading` module that can be used to synchronize access to shared resources between threads. Here's an example of using a lock to synchronize access to a shared variable:

```python
import threading

counter = 0

lock = threading.Lock()

def increment_counter():
    global counter
    lock.acquire()
    counter += 1
    lock.release()

# Create multiple threads to increment the counter

threads = []

for _ in range(10):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

# Wait for all threads to finish

for t in threads:
    t.join()

print(counter)

```

In this example, we define a shared variable `counter` and a `Lock` object `lock` to synchronize access to the counter. We then create 10 threads that increment the counter using the `increment_counter` function. The `lock.acquire()` and `lock.release()` methods are used to acquire and release the lock, ensuring that only one thread can access the counter at a time.

#### Practical Exercises

1. Write a Python program that creates two threads, one that prints even numbers from 1 to 10, and another that prints odd numbers from 1 to 10. Use thread synchronization to ensure that the threads alternate in printing the numbers.

2. Write a Python program that simulates a bank account with a shared balance. Create multiple threads that deposit and withdraw money from the account, ensuring that the balance is updated correctly

3. Write a Python program that uses threads to download multiple files concurrently from a list of URLs. Use thread synchronization to ensure that the files are downloaded in parallel without conflicts.

#### Assignment

Create a Python program that simulates a simple chat application using threads. The program should have a server thread that listens for incoming messages from clients, and multiple client threads that send messages to the server. Use thread synchronization to ensure that messages are sent and received correctly between the server and clients.

#### Resources

- [Python threading module documentation](https://docs.python.org/3/library/threading.html)
- [Real Python - Python Threading](https://realpython.com/intro-to-python-threading/)
- [GeeksforGeeks - Python Multithreading](https://www.geeksforgeeks.org/multithreading-python-set-1/)
- [Tutorialspoint - Python Multithreading](https://www.tutorialspoint.com/python/python_multithreading.htm)
