from django.db import models

class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    