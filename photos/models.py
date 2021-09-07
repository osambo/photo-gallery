from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length =30)

    # def __str__(self):
    #     return self.name

    @classmethod
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return f'Name: {self.name}'

class Image_Location (models.Model):
    name = models.CharField(max_length=30)
    
    # def __str__(self):
    #     return self.name
    def __str__(self):
        return f'Name: {self.name}'

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    Image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length =60)
    Description = models.TextField()
    categories= models.ForeignKey(Categories,on_delete=models.CASCADE)
    location = models.ForeignKey(Image_Location,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos
    
    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(pub_date__date = date)
        return photos
    
    @classmethod
    def search_by_category(cls, categories):
        Image = cls.objects.filter(categories__name__icontains=categories)
        return Image

    @classmethod
    def save_Image (cls):
        photos=cls.objects.filter()
        return photos

    @classmethod
    def delete_Image (cls):
        photos=cls.objects.filter()
        return photos

    @classmethod
    def update_image(self, name=name, category=None):
        self.name = name if name else self.name
        self.categories = categories if categories else self.categori

        self.save()
    
    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def filter_by_location(cls, location):
        Image_Location = Image.objects.filter(location__name=location).all()
        return  Image_Location

    @classmethod
    def search_image(cls, key):
        Image = cls.objects.filter(
            cls(description__contains=key) | cls(Name__icontains=key) | cls(location__place__icontains=key))
        print(Image)
        return Image

    def __str__(self):
        return self.name