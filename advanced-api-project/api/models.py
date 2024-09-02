from django.db import models

class Author(models.Model):
    # This model represents an author in the system.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    # This model represents a book, which is linked to an author.
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
