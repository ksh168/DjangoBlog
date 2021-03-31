from django.db import models
from django.contrib.auth.models import User

#to resize image
from PIL import Image

class Profile(models.Model):
    #make a one to one relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #to resize/compress large images
    #overiding existing parent class method
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            #make image of size 300x300
            img.thumbnail(output_size)
            #overwrite over existing image
            img.save(self.image.path)