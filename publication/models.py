from django.db import models

from authentication.models import CustomUser


# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    publisher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title + ' - ' + self.publisher.username

class Like(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_liked = models.BooleanField()

    class Meta:
        unique_together = ('publication', 'author')
    def __str__(self):
        return self.author.username + ' - ' + self.publication.title