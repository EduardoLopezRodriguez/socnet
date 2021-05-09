from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.width > 150:

            output_size = (img.height, 150)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
