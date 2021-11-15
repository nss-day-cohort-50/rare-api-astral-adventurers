from django.db import models
from django.db.models.expressions import F


class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    publication_date = models.DateField()
    is_published = models.BooleanField(default=False)
    image_url = models.ImageField()
    content = models.TextField()
    approved = models.BooleanField(default=False) 