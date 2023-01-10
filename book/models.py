from django.db import models


class Book(models.Model):
    GENRE = (
        ("Detective", "Detective"),
        ("Horror", "Horror"),
        ("Anime", "Anime"),
        ("Comedy", "Comedy"),
        ("Document", "Document"),
        ("Fantasy", "Fantasy"),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    description = models.TextField()
    quantity = models.PositiveIntegerField(null=True)
    genre = models.CharField(max_length=100, choices=GENRE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentBook(models.Model):
    choice_book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comment_object"
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
