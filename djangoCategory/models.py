from django.db import models

# Create your models here.
class Categories(models.Model):
    title=models.CharField(max_length=20)
    address=models.CharField(max_length=20)

    class Meta():
        verbose_name_plural="Categories"

    def __str__(self):
        return self.title