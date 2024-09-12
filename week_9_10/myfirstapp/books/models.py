from mongoengine import Document, StringField, DateField

class Book(Document):
    title = StringField(required=True, max_length=200)
    author = StringField(required=True, max_length=100)
    published_date = DateField(required=True)

    def __str__(self):
        return self.title
