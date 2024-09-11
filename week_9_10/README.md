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

Lets do some coding:

```python
# models.py

from mongoengine import Document, StringField, IntField

class Book(Document):
    title = StringField(required=True)
    author = StringField(required=True)
    year = IntField()

# views.py

from .models import Book

def create_book(request):
    book = Book(title="Django for Beginners", author="William Vincent", year=2020)
    book.save()
    return HttpResponse("Book created successfully!")

def get_books(request):

    # Get all books
    books = Book.objects()

    return JsonResponse({"books": books})
```

#### Add mongo atlas URL for mongoengine

```python
from mongoengine import *

connect('MONGO_URL')


```
