from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    about = models.TextField()

    class Meta:
        db_table = 'Author'

    def __str__(self):
        return self.name


class Genres(models.Model):
    genre_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Genres'

    def __str__(self):
        return self.genre_name


class Books(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    ISBN = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='book_images/')
    release_date = models.DateField()
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Books'

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        db_table = 'BookAuthor'

    def __str__(self):
        return self.author.name


class Reviews(models.Model):
    star_given = models.IntegerField()
    user = models.CharField(max_length=100)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    body = models.TextField(default=" ")

    class Meta:
        db_table = 'Reviews'

    def __str__(self):
        return self.book.name
