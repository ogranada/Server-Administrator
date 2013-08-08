from django.db import models
from django.contrib.auth.models import User
import datetime

class Backup(models.Model):

    class Meta:
        verbose_name_plural = "Backup"

    date = models.DateTimeField(default=datetime.datetime.today())
    description = models.TextField(max_length=30)
    user = models.ForeignKey(User)


    def __str__(self):
    	today = datetime.datetime.now()
    	date = str(self.date.date().isoformat() if self.date.date()!=today.date() else self.date.time().isoformat().split('.')[0])
        return self.description+"("+date+")"

