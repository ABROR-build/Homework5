from django.forms import ModelForm
from . import models


class CreateAuthor(ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'


class AddBook(ModelForm):
    class Meta:
        model = models.Books
        fields = '__all__'


class BookAuthorMatch(ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = '__all__'
