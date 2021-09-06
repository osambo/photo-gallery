from django.test import TestCase
from .models import Image,Categories,Image_Location
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new tag and saving it

        self.new_categories = categories(name = 'testing')
        self.new_category.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post')
        self.new_image.save()

        self.new_image.categories.add(self.new_categories)

    def tearDown(self):
        categories.objects.all().delete()
        Image.objects.all().delete()

    def test_get_photos_today(self):
        today_photos = Image.todays_photos()
        self.assertTrue(len(today_photos)>0)

    def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        photos_by_date = Image.days_photos(date)
        self.assertTrue(len(photos_by_date) == 0)

# Location tests
class Location(TestCase):
    def setUp(self):
        self.new_location = Location(place='Nairobi')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def save_location(self):
        before = Location.objects.count()
        self.new_location.save_location()
        after = Location.objects.count()
        self.assertTrue(before < after)

    def tearDown(self):
        Location.objects.all().delete()


# Testing image class
class TestImage(TestCase):
    def setUp(self):
        self.category = Category(name='cars')
        self.category.save()

        self.location = Location(place='juja')
        self.location.save_location()

        self.new_image = Image(name='Bmw', description='A perfect Bmw', category=self.category, location=self.location,
                               submitted=datetime.date.today(), url='images/bmw.jpg')

    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_image_update(self):
        pass

    def test_image_id(self):
        pass

    def test_search_image(self):
        pass

    def test_save_image(self):
        before = Image.objects.count()
        self.new_image.save_image()
        after = Image.objects.count()
        self.assertTrue(before < after)

    def test_search_by_title(self):
        pass

    def tearDown(self):
        Image.objects.all().delete()