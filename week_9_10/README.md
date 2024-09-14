# Week 9 and 10 - Database Integration in Django

### 1. Databases

- **Definition**: Organized collections of data that are easily accessible, managed, and updated.
- **Key Concepts**:
  - **Relational Databases**: Use structured schema and tables to define relationships.
  - **Non-Relational Databases**: Allow for unstructured or semi-structured data storage.
  - **ACID Properties**: Atomicity, Consistency, Isolation, Durability – principles of reliable transaction processing.
  - **CAP Theorem**: In distributed databases, you can only achieve two out of three: Consistency, Availability, Partition tolerance.
- **Types of Operations**: CRUD (Create, Read, Update, Delete), indexing, partitioning, sharding.

### 2. API and Databases

- **API Definition**: An Application Programming Interface (API) allows different software systems to communicate with each other.
- **Database Interaction**: APIs provide endpoints for database operations like fetching, adding, or updating data.
- **Common Types**:
  - **RESTful APIs**: Communicates with databases using HTTP requests (GET, POST, PUT, DELETE).
  - **GraphQL**: A more flexible alternative to REST that allows clients to query exactly what they need.
- **Security**: API/database security involves authentication (OAuth, JWT), rate limiting, and preventing SQL injection attacks.
- **Example**: An API that interacts with a database to retrieve user data based on a request, such as fetching product information in an e-commerce app.

### 3. Types of Databases

- **Relational Databases (SQL)**:
  - Stores data in tables with structured relationships.
  - Examples: MySQL, PostgreSQL, Oracle, SQL Server.
- **Document-Oriented Databases (NoSQL)**:
  - Stores data as documents, typically in JSON or BSON formats.
  - Examples: MongoDB, CouchDB.
- **Key-Value Stores**:
  - Simple storage of key-value pairs for fast lookups.
  - Examples: Redis, DynamoDB.
- **Column-Family Databases**:
  - Organizes data into columns and is designed for high-volume reads/writes.
  - Examples: Cassandra, HBase.
- **Graph Databases**:
  - Focuses on relationships between entities, representing data as nodes and edges.
  - Examples: Neo4j, ArangoDB, Dgraph

### 4. SQL (Structured Query Language)

- **Definition**: A domain-specific language used for managing and querying relational databases.
- **Key Concepts**:
  - **Tables**: Data is stored in rows and columns.
  - **Primary and Foreign Keys**: Used to establish relationships between tables.
  - **CRUD Operations**: Create (INSERT), Read (SELECT), Update (UPDATE), and Delete (DELETE).
  - **Joins**: Combining data from multiple tables (INNER JOIN, LEFT JOIN, etc.).
  - **Transactions**: Ensuring data integrity with COMMIT and ROLLBACK.
  - **Normalization**: Organizing tables to reduce redundancy.
- **Common SQL Databases**: MySQL, PostgreSQL, SQL Server, Oracle.

### 5. NoSQL (Not Only SQL)

- **Definition**: A broad category of databases designed for more flexible data models, often used for big data and real-time web applications.
- **Key Concepts**:
  - **Data Models**: Key-Value, Document, Column-Family, Graph databases.
  - **Scalability**: Horizontal scaling, better suited for large-scale distributed systems.
  - **Schema Flexibility**: Unlike SQL, NoSQL databases can store unstructured or semi-structured data.
  - **Eventual Consistency**: Prioritizes availability and partition tolerance over immediate consistency.
- **Common NoSQL Databases**: MongoDB, Cassandra, Couchbase, DynamoDB, Redis.

### 6. Famous Databases

- **MySQL**: A widely-used open-source relational database.
- **PostgreSQL**: Known for its advanced features and strong support for complex queries.
- **MongoDB**: A popular NoSQL document-oriented database.
- **Redis**: An in-memory key-value store used for caching and real-time applications.
- **Cassandra**: A scalable NoSQL column-family database used for big data applications.
- **DynamoDB**: Amazon's managed NoSQL key-value store with high availability and scaling.

## Database Integration in Django with MongoEngine

### 1. Django ORM vs. MongoEngine

- **Django ORM**:

  - Built-in Object-Relational Mapping (ORM) for SQL databases.
  - Uses models to define database tables and relationships.
  - Supports migrations, queries, and transactions.

- **MongoEngine**:
  - An Object-Document Mapper (ODM) for MongoDB.
  - Allows Django to interact with MongoDB using models.
  - Supports document-based queries and schema-less data.

### 2. Setting Up MongoEngine

- **Installation**: Install `mongoengine` using pip.

  ```bash
  pip install mongoengine
  ```

- **Configuration**:

  - Add `mongoengine` to `INSTALLED_APPS` in Django settings.
  - Configure MongoDB connection settings in `settings.py`.

- **Defining Models**:

  - Create models that inherit from `Document` in MongoEngine.
  - Define fields using `mongoengine` data types.

### 3. Querying MongoDB with MongoEngine

- **Basic Queries**:

  - Use model methods like `save()`, `find()`, `get()`, `update()`, and `delete()`.
  - Filter results using query operators like `__lt`, `__gt`, `__contains`.

- **Aggregation**:

  - Perform aggregation operations like `group`, `sum`, `count`, and `aggregate`.

- **Indexes**:

  - Improve query performance by creating indexes on fields.
  - Use `ensure_index()` to create indexes in MongoEngine.

  What is indexing in databases?

  - **Definition**: Indexing is a technique used to improve the speed of data retrieval operations on a database table.

  - **Easy to understand Example**: Imagine you have a library with thousands of books. If you want to find a specific book, you could search through each book one by one until you find the right one. This is like searching without an index. However, if you create an index (like an alphabetical list of book titles), you can quickly jump to the right section and find the book much faster.

  - **Key Benefits**:
    - **Faster Queries**: Indexes allow the database to quickly locate the rows that match a query.
    - **Reduced Disk I/O**: Indexes can reduce the amount of data that needs to be read from disk.
    - **Optimized Performance**: Queries that use indexes can be significantly faster than full table scans.

#### Lets do some coding

To create a Django REST API with MongoDB using mongoengine instead of the default Django ORM, you'll need to adjust the project to use MongoDB as your database. Here's how to implement the Book model, along with CRUD operations for GET, POST, PUT, and DELETE using mongoengine and Django Rest Framework (DRF).

##### Step 1: Install the Required Packages

First, install the necessary packages for Django, mongoengine, and Django Rest Framework.

```bash
pip install django mongoengine djangorestframework djongo
```

##### Step 2.1: Create a Django Project and App

Create a new Django project and app using the following commands:

```bash
python -m django startproject bookstore
cd bookstore
python manage.py startapp books
```

##### Step 2.2: Configure MongoDB Connection

In the `settings.py` file of your Django project, configure the MongoDB connection using the `DATABASES` setting. Replace the default SQLite configuration with the following:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'bookstore',
    }
}

MONGODB_SETTINGS = {
    'db': 'your_mongo_db_name',
    'host': 'localhost',
    'port': 27017,
}
```

if you are using srv connection string then you can use the following configuration

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'bookstore',
    }
}

MONGODB_DATABASES = {
    'default': {
        'name': 'your_mongo_db_name',
        'host': 'your_mongo_db_connection_string',
        'username': 'your_mongo_db_username',
        'password': 'your_mongo_db_password',
        'authentication_source': 'admin',
    }
}
```

##### Step 3: Define the Book Model

Create a `models.py` file in the `books` app and define the `Book` model using mongoengine.

```python
# books/models.py
import mongoengine as me

class Book(me.Document):
    title = me.StringField(required=True, max_length=200)
    author = me.StringField(required=True, max_length=100)
    published_date = me.DateTimeField(required=True)

    def __str__(self):
        return self.title
```

Here, me.Document is the base class for mongoengine documents, and fields like StringField and DateTimeField are used for creating schema definitions.

##### Step 4: Create Serializers for the Book Model

Next, create serializers for the Book model using Django Rest Framework.

```python

# books/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()

    def create(self, validated_data):
        return Book(**validated_data).save()

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance
```

##### Step 5: Create Views for CRUD Operations

Create views for performing CRUD operations on the Book model using Django Rest Framework.

```python
# books/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=204)
```

##### Step 6: Register the Views in the URLs

Finally, register the BookViewSet in the `urls.py` file of the `books` app.

```python

# books/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
```

Then, include this in your project's urls.py:

```python

# bookstore/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
]
```

##### Step 7: Run the Server and Test the API

Run the Django development server using the following command:

```bash
python manage.py runserver
```

You can now test the API endpoints for CRUD operations on the Book model using tools like Postman or curl.

##### Step 8: Example API Requests

Here are some example API requests you can make to test the CRUD operations:

- **GET /api/books/**: Retrieve a list of all books.
- **GET /api/books/{id}/**: Retrieve a specific book by ID.
- **POST /api/books/**: Create a new book.
- **PUT /api/books/{id}/**: Update an existing book.
- **DELETE /api/books/{id}/**: Delete a book by ID.

- Create a new book (POST)

```bash
curl -X POST http://127.0.0.1:8000/api/books/ \
-H "Content-Type: application/json" \
-d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_date": "1925-04-10"
}'
```

- Get all books (GET)

```bash
curl http://127.0.0.1:8000/api/books/
```
