from django.db import models

class Petshop(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_images = models.ImageField(upload_to='pet_images/')

    def __str__(self):
        return self.pet_name
    

    

# Create your models here.
