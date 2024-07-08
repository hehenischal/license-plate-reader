from django.db import models
from home.utils import extract_number

# Create your models here.

class NumberPlate(models.Model):
    number_plate = models.ImageField(upload_to='number_plate/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.date)
    
    @property
    def get_absolute_image_url(self):
        return f"{self.number_plate.url}"
    
    @property
    def extract_number_plate(self):
        return extract_number(self.number_plate.path)
    