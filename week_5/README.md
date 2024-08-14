## Week 5: Introduction to Django Framework

### REST API

- REST stands for Representational State Transfer.
- REST is web standards based architecture and uses HTTP Protocol.
- It revolves around resource where every component is a resource and a resource is accessed by a common interface using HTTP standard methods.
- REST was first introduced by Roy Fielding in 2000.
- A REST Server simply provides access to resources and REST client accesses and modifies the resources using HTTP protocol.
- Here each resource is identified by URIs/ global IDs. REST uses various representation to represent a resource like text, JSON, XML. JSON is the most popular one.
- REST follows the object-oriented programming paradigm of noun-verb.

#### HTTP Methods

- GET - GET is used to request data from a specified resource.
- POST - POST is used to send data to a server to create/update a resource.
- PUT - PUT is used to send data to a server to create/update a resource.
- DELETE - DELETE is used to delete a specified resource.

#### Routing

- Routing refers to how an application’s endpoints (URIs) respond to client requests.
- You define routing in Django using the URL dispatcher and views. For example, using path() in the urls.py file to handle different request types.
- Django supports various HTTP methods like GET, POST, and others.
- There is a special routing decorator @csrf_exempt which can be used to exempt a view from the CSRF verification.

#### Route Methods

Route methods are defined in views and connected to URLs using the URL dispatcher.
The following code is an example of routes that are defined for the GET and the POST methods to the root of the app.

```python
# views.py

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# GET method route
def home_get(request):
    if request.method == 'GET':
        return HttpResponse("GET request to the homepage")

# POST method route
@csrf_exempt
def home_post(request):
    if request.method == 'POST':
        return HttpResponse("POST request to the homepage")
```

```python
# urls.py

from django.urls import path
from .views import home_get, home_post

urlpatterns = [
    path('', home_get),
    path('post/', home_post),
]

```

### Route Paths

- Route paths, in combination with a request method, define the endpoints at which requests can be made.
- Route paths are defined as strings in the urls.py file.

Here are some examples of route paths based on strings.

```python

# views.py

from django.http import HttpResponse

# This view will match requests to the root route, /.

def root_view(request):
return HttpResponse("root")

# This view will match requests to /about.

def about_view(request):
return HttpResponse("about")

# This view will match requests to /random.text.

def random_text_view(request):
return HttpResponse("random.text")

```

```python
# urls.py

from django.urls import path
from .views import root_view, about_view, random_text_view

urlpatterns = [
path('', root_view),
path('about/', about_view),
path('random.text', random_text_view),
]
```

In these examples:

- The views.py file contains the view functions that return HttpResponse for the respective routes.
- The urls.py file maps the URL patterns to the corresponding view functions using the path() function from django.urls.

### Route Parameters

- Route parameters are named URL segments that are used to capture the values specified at their position in the URL.
- The captured values are passed as arguments to the view functions.
- Route path: `/users/<int:userId>/books/<int:bookId>`
- Request URL: `http://localhost:8000/users/34/books/8989`
- Captured parameters: userId is `34` and bookId is `8989`

```python
# views.py

from django.http import HttpResponse
from django.shortcuts import render

def user_books(request, userId, bookId):
    response = {
        "userId": userId,
        "bookId": bookId
    }
    return HttpResponse(str(response))
```

```python
# urls.py

from django.urls import path
from .views import user_books

urlpatterns = [
    path('users/<int:userId>/books/<int:bookId>/', user_books),
]
```

### Route Handlers

- You can use multiple view functions to handle a request.
- Middleware and decorators can be used to impose pre-conditions on a route and pass control to subsequent views if there’s no reason to proceed with the current view.

````python

# views.py

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class PrintMiddleware(MiddlewareMixin):
def process_request(self, request):
print("PrintMiddleware: Request intercepted")
return None

def example_a(request):
return HttpResponse("Hello from A!")

def example_b1(request):
print("The response will be sent by the next function ...")
return HttpResponse("Hello from B!")

def example_c0(request):
print("CB0")
return None

def example_c1(request):
print("CB1")
return None

def example_c2(request):
return HttpResponse("Hello from C!")

def example_d0(request):
print("CB0")
return None

def example_d1(request):
print("CB1")
return None

def example_d2(request):
print("The response will be sent by the next function ...")
return None

def example_d3(request):
return HttpResponse("Hello from D!")

```python

# urls.py

from django.urls import path
from .views import example_a, example_b1, example_c0, example_c1, example_c2, example_d0, example_d1, example_d2, example_d3

urlpatterns = [ # A single view function can handle a route. For example:
path('example/a/', example_a),

    # More than one view function can handle a route (using middleware-like behavior). For example:
    path('example/b/', example_b1),

    # A list of view functions can handle a route. For example:
    path('example/c/', lambda request: (example_c0(request), example_c1(request), example_c2(request))[-1]),

    # A combination of independent functions and lists of functions can handle a route. For example:
    path('example/d/', lambda request: (example_d0(request), example_d1(request), example_d2(request), example_d3(request))[-1]),

]
````

In these examples:

The views.py file contains the view functions that handle the requests.
The urls.py file maps the URL patterns to the corresponding view functions.
Middleware-like behavior is simulated using lambdas to sequentially call functions in the URL patterns.

# Overview of Django Framework

Django is a high-level Python web framework that enables the rapid development of secure and maintainable websites. It was designed to help developers take applications from concept to completion as quickly as possible.

## Understanding the History and Purpose of Django

Django was created in 2003 by web developers Adrian Holovaty and Simon Willison at the Lawrence Journal-World newspaper. It was released publicly under a BSD license in July 2005. The primary goal of Django is to ease the creation of complex, database-driven websites by emphasizing reusability and "pluggability" of components.

## Exploring the Features and Advantages of Django

- **Fast Development:** Django promotes rapid development with its "batteries-included" philosophy, meaning it comes with many built-in features.
- **Security:** Django helps developers avoid common security mistakes, such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).
- **Scalability:** Django's ability to handle large amounts of traffic and its use by major websites (e.g., Instagram, Pinterest) demonstrate its scalability.
- **Versatility:** Django can be used for various types of projects, from content management systems to social networks to scientific computing platforms.

## Setting Up a Django Project

### Installation and Configuration of Django

First, ensure you have Python installed. You can install Django using pip:

```bash
pip install django
```

### Creating a New Django Project

To create a new Django project, use the `django-admin` command:

```bash
django-admin startproject myproject
cd myproject
```

### Exploring Project Structure and Files

The `myproject` directory will contain the following structure:

```markdown
myproject/
manage.py
myproject/
**init**.py
settings.py
urls.py
wsgi.py
```

- manage.py: A command-line utility for interacting with the Django project.
- settings.py: Configuration settings for the project.
- urls.py: URL declarations for the project.
- wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.

## MVC Architecture in Django

### Understanding the Model-View-Controller (MVC) Pattern

Django follows the Model-View-Controller (MVC) architectural pattern, which separates an application into three main components:

- Model: The data layer, which defines the data structure.
- View: The presentation layer, which displays the data to the user.
- Controller: The logic layer, which processes user input and interacts with the model.

In Django, the terminology is slightly different but follows the same principles:

- Model: Defines the data structure (same as MVC).
- View: Manages what data is presented to the user and how it is displayed (similar to Controller in MVC).
- Template: The presentation layer (similar to View in MVC).

### Implementing MVC in Django

Role of Models, Views, and Templates in Django Applications

- Models: Define the structure of your data and provide an API for interacting with it.
- Views: Handle the logic for your application, process requests, and return responses.
- Templates: Define the HTML structure of the webpage and display data passed from views.

### Coding Example

Let's create a simple Django application that displays a list of books.

_Step 1: Create an App_

```bash
python manage.py startapp books
```

_Step 2: Define a Model_

In `books/models.py`:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

_Step 3: Register the Model_

In `books/admin.py:`

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

_Step 4: Create Views_

In `books/views.py`:

```python

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

```

_Step 5: Define URL Patterns_

In `books/urls.py:`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
]
```

Include the app URLs in the main project urls.py:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]
```

_Step 6: Create Templates_

In `books/templates/books/book_list.html:`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Book List</title>
  </head>
  <body>
    <h1>Book List</h1>
    <ul>
      {% for book in books %}
      <li>{{ book.title }} by {{ book.author }} ({{ book.published_date }})</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

##### Run Migration

```bash
python manage.py makemigrations books
python manage.py migrate
```

#### Running the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/books/` to see the list of books.
