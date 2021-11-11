from django.contrib.auth.models import User
from django.db import models

from io import BytesIO
from PIL import Image
from django.core.files import File
from django.utils.text import slugify

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=slugify(name))
    display_name = models.CharField(max_length=255, default=name)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE,blank=True, null=True) # linking venders to users, and making sure they get deleted when the users do
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta: # this allows us to order by name
        ordering = ['name']
    
    def __str__(self): # this is a string representation - we see the vendor name instead of the object ID
        return self.name
    
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
        img.convert('RGB')
        img.thumbnail(size) # using inbuilt thumbnail generator function

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85) # save the image in JPEG format

        thumbnail = File(thumb_io, name=image.name) # turn the image object into a file

        return thumbnail
    
    # def save(self, *args, **kwargs): # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)