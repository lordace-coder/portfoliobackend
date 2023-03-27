from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model



user = get_user_model()
# model that keeps count of the users malicious attempts
class Malicious_count(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    mal_count = models.IntegerField(default=0)

    def mal_user_spotted(self):
        self.mal_count +=1
        self.save()
        return f'updated {self.user.username}s mal count'