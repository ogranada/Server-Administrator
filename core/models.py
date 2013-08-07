from django.db import models

# Create your models here.

class Applications(models.Model):

    class Meta:
        verbose_name_plural = "Applications"

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class MenuItems(models.Model):

    class Meta:
        verbose_name_plural = "Menu Items"

    name = models.CharField(max_length=100)
    description = models.TextField()
    app_path = models.CharField(max_length=200)
    application = models.ForeignKey(Applications)

    def __str__(self):
        return self.name







