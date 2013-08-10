from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext as _

# Create your models here.

class Application(models.Model):

    class Meta:
        verbose_name_plural = "Applications"
        ordering = ['position']

    name = models.CharField(max_length=100)
    description = models.TextField()
    position = models.IntegerField()

    def __str__(self):
        return _(self.name)


class MenuItem(models.Model):

    class Meta:
        verbose_name_plural = "Menu Items"

    name = models.CharField(max_length=100)
    description = models.TextField()
    app_path = models.CharField(max_length=200)
    application = models.ForeignKey(Application)

    def __str__(self):
        return _(self.name)

class Server(models.Model):

    class Meta:
        verbose_name_plural = "Servers"

    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return _(self.name)





