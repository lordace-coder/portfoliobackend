from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


user = get_user_model()

class Users_messages(models.Model):
    senders_name=models.ForeignKey(user,on_delete=models.CASCADE)
    msg_txt = models.TextField(blank=False)
    

    def __str__(self):
        return self.senders_name.username
    class Meta:
        verbose_name_plural = "Users_messages"
        verbose_name = "Users_message"

