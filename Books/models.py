from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='author_added_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='author_changed_by')

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='publication_added_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='publication_changed_by')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey(to="self", on_delete=models.SET_NULL, null=True, related_name='pcategory')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='category_added_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='category_changed_by')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    publication = models.ForeignKey(to=Publication, on_delete=models.SET_NULL, null=True, related_name='publisher')
    author = models.ManyToManyField(to=Author)
    category = models.ManyToManyField(to=Category)
    quantity = models.IntegerField(default=1)
    available_quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='books_added_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='books_changed_by')

    def __str__(self):
        return f"{self.name} is published by {self.publication.name} and written by {self.authors()}"

    def authors(self):
        return ",".join([x.name for x in self.author.all()])

