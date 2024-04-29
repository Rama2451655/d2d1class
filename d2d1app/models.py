from django.db import models
class Table(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/', height_field=800, width_field=1100, max_length=None)
    date=models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
    