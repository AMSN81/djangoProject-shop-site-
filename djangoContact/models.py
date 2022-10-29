from django.db import models

# Create your models here.
class Contact_us(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=30)
    text=models.TextField()
    is_read=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="Contact_us"

    def __str__(self):
        return self.subject

