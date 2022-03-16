from django.db import models
from django.contrib.auth.models import User

from io import BytesIO
from PIL import Image
from django.core.files import File
from django.http.response import Http404
from django.utils.text import slugify

from apps.core.models import User

class Vendor(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE) # linking venders to users, and making sure they get deleted when the users do
    display_name = models.CharField(max_length=255, default=created_by.name)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    g_rating = models.FloatField(default=None, blank=True, null=True)
    g_review_count = models.IntegerField(default=0)
    
    class Meta: # this allows us to order by name
        ordering = ['display_name']
    
    def __str__(self): # this is a string representation - we see the vendor name instead of the object ID
        return self.display_name
    
    def get_thumbnail(self): # Checks whether a thumb nail exists
        if self.thumbnail: # if the thumbnail already exists we don't need to do anything
            return self.thumbnail.url
        else:
            if self.image: # if an image does exist, pass it to the create a thumbnail function
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else: # if an image doesn't exist, use a placeholder
                return 'https://via.placeholder.com/300.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)): # generates a thumbnail from a given image
        img = Image.open(image) # create an image object
        rgb_img = img.convert('RGB')
        rgb_img.thumbnail(size) # using inbuilt thumbnail generator function

        thumb_io = BytesIO()
        rgb_img.save(thumb_io, 'JPEG', quality=85) # save the image in JPEG format

        thumbnail = File(thumb_io, name=image.name) # turn the image object into a file

        return thumbnail
    
    # def save(self, *args, **kwargs): # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)