from django.db import models
from django.contrib.auth.models import AbstractUser
from app1.models import *


class User(AbstractUser):
    choices = (('wilaya', 'wilaya'), ('kata', 'kata'), ('mtaa', 'mtaa'))
    type = models.CharField(max_length=10, choices=choices)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username


# class Profile(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
#     mtaa = models.ForeignKey(Mtaa, on_delete=models.CASCADE)
#     kata = models.ForeignKey(Kata, on_delete=models.CASCADE)
#     wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.user_id.username}'
