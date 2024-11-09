from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) #ekta post multiple category er moddhe thakte pare abar ekta category er moddhe multiple post thakte pare
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #many to one deyar jonno foreignkey use kora hoy. r on_delete=models.CASCADE use korsi jodi author tar profile delete kore then tar blog post gulao delete hoye jabe.
    
    def __str__(self):
        return self.title