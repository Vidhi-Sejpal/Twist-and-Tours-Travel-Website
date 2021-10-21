from django.db import models
from ckeditor.fields import RichTextField


class Travel_Destination(models.Model): 

    trip_options = (
    ('Choose' ,'Choose'),
    ('Trending Trips' ,'Trending Trips'),
    ('Weekend Trips','Weekend Trips'),
    ('Backpacking Trips','Backpacking Trips'),
    ('Treks','Treks')
    )

    trip_id = models.AutoField
    trip_title = models.CharField(max_length=100,blank=False,null=False)
    trip_choice = models.CharField(max_length=50,choices = trip_options,default = trip_options[0][0],blank=False,null=False)
    trip_drive_link = models.CharField(max_length=250,blank=False,null=False,default='#')
    trip_days =  models.IntegerField(default=0)
    trip_description = models.TextField(blank = True)
    trip_price = models.IntegerField(default=0)
    trip_location = models.CharField(max_length=100,blank=False,null=False)
    trip_image = models.ImageField(upload_to='tnt/Travel_Destination',blank=False,null=False,default='')

    def __str__(self):
        return self.trip_title

class Review(models.Model):
    review_id = models.AutoField
    user_name = models.CharField(max_length=100,blank=False,null=False)
    review_description = models.TextField(blank = True)
    user_image = models.ImageField(upload_to='tnt/Reviews',blank=False,null=False,default='')

    def __str__(self):
        return self.user_name

class Blog(models.Model):

    user_id = models.AutoField
    blog_image = models.ImageField(upload_to='tnt/Blogs',blank=False,null=False,default='')
    blog_title = models.CharField(max_length=100,blank=False,null=False)
    user_name = models.CharField(max_length=100,blank=False,null=False)
    user_image = models.ImageField(upload_to='tnt/Blogs',blank=False,null=False,default='')
    blog_description = RichTextField(blank=False,null=False)
    blog_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user_name

class Gallery(models.Model):
    gallery_id = models.AutoField
    gallery_image = models.ImageField(upload_to='tnt/Gallery',blank=False,null=False,default='')
    gallery_title = models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return self.gallery_title
