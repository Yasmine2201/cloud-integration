from django.db import models
from core_models.models import User


class Publication(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + self.publisher.username

class Like(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('publication', 'author')
    def __str__(self):
        return self.author.username + ' - ' + self.publication.title