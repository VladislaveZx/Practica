from django.db import models

class Users(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=25)

    def __str__(self):
        return self.telegram_id, self.username, self.full_name
