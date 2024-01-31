from django.db import models

# Create your models here.
class Movie(models.Model): 
    movie_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=10)
    type = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    languages = models.CharField(max_length=50)
    movie_poster = models.ImageField(upload_to='images')
    dimension = models.CharField(max_length=50)
    about_movie = models.TextField(max_length=500)

class Location(models.Model):
    location = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Theatre(models.Model):
    theatre_name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Premium_Movie(models.Model):
    premiere_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=10)
    type = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    languages = models.CharField(max_length=50)
    premiere_poster = models.ImageField(upload_to='images')
    rent_cost = models.IntegerField()
    buy_cost = models.IntegerField()
    about_movie = models.TextField(max_length=500)

class Movie_cast(models.Model):
    name = models.CharField(max_length=50)
    role_name = models.CharField(max_length=50)
    cast_image = models.ImageField(upload_to='images')
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    

class Events(models.Model):
    event_name = models.CharField(max_length=50)
    domain = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=50, null=True)
    started_at = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    duration = models.CharField(max_length=50, null=True)
    language = models.CharField(max_length=50)
    cost = models.IntegerField()
    event_poster = models.ImageField(upload_to='images')
    place = models.CharField(max_length=50, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class User(models.Model):
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=6)
    pincode = models.IntegerField()
    address = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to='images', default='images/p1.png')
    password = models.CharField(max_length=10,null=True)

class Payment(models.Model):
    filter_prize = models.IntegerField()
    no_of_tickets = models.IntegerField()
    total_cost = models.IntegerField()
    email = models.EmailField(default="ex@gmail.com")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Adds(models.Model):
    add_poster= models.ImageField(upload_to='images')




    
