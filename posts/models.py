from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) #ekta post multiple category er moddhe thakte pare abar ekta category er moddhe multiple post thakte pare
    author = models.ForeignKey(User, on_delete=models.CASCADE) #many to one deyar jonno foreignkey use kora hoy. r on_delete=models.CASCADE use korsi jodi author tar profile delete kore then tar blog post gulao delete hoye jabe.
    image = models.ImageField(upload_to='posts/media/uploads/', blank =True, null = True)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)#jokhon ei class er object create hobe tokhon sei time ta rekhe dibe. 
    
    def __str__(self):
        return f"comments by {self.name}"