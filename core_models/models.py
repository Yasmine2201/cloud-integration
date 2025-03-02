from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return super().__str__() + ' ' + self.email