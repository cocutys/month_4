from django.db import models

class Book(models.Model):
    GENRE = (
        ('Detective', 'Detective'),
        ('Horror', 'Horror'),
        ('Anime', 'Anime'),
        ('Comedy', 'Comedy'),
        ('Document', 'Document'),
        ('Fantasy', 'Fantasy')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    quantity = models.PositiveIntegerField(null=True)
    genre = models.CharField(max_length=100, choices=GENRE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
