from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    services_offered = models.CharField(max_length=50000)
    pricing = models.CharField(max_length=200)
    ambulance_available = models.BooleanField(default=False)
    ambulance_contacts = models.CharField(max_length=50000)
    vacancies_available = models.BooleanField(default=False)
    ratings = models.FloatField()
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default = True)
    home_general = models.BooleanField(default = False)
    home_specialty = models.BooleanField(default = False)
    home_psychiatric = models.BooleanField(default = False)
    home_clinic = models.BooleanField(default = False)
    affordable = models.BooleanField(default = False)
    top_rated = models.BooleanField(default = False)
    new = models.BooleanField(default = False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.hospital_name
    

class MedicalStaff(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    