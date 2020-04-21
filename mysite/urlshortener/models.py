from django.db import models
import random
import string
# Create your models here.

def shorten(length=8):
    letters = string.ascii_lowercase + string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(length))


class URLManager(models.Manager):

    def create_url(self, engine):
        shortcut = shorten(8)
        url_object = self.create(engine=engine, shortcut=shortcut)
        return url_object



class URLs(models.Model):
    engine = models.CharField(max_length=2048, primary_key=True)
    shortcut = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True)

    objects = URLManager()

    def __str__(self):
        return f"{self.engine} => {self.shortcut}"
