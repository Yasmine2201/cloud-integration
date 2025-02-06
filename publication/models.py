from django.db import models

from authentication.models import CustomUser


# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    publisher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=True) # a user can only have one publication
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title + ' - ' + self.publisher.username

class Comment(models.Model):
    body = models.TextField()
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.body + ' - ' + self.author.username

class Like(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.author.username + ' - ' + self.publication.title