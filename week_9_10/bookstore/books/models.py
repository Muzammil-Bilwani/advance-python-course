import mongoengine as me

class Book(me.Document):
    title = me.StringField(required=True, max_length=200)
    author = me.StringField(required=True, max_length=100)
    published_date = me.DateTimeField(required=True)

    def __str__(self):
        return self.title