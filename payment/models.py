from django.db import models

# Create your models here.
class Payments (models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    email=models.CharField(default="null@email.com" , max_length=100)
    payment_id=models.CharField(max_length=100)
   
    paid=models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
