from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(null=True)
    description = models.TextField(null=True)
    content = models.TextField(null=True)
    image = models.ImageField(null=True)
    slug = models.SlugField(default='', null=True, db_index=True)

    #
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('post-name', args=[self.slug])

    def __str__(self):
        return f"{self.title} - {self.description}"


class AboutMe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    full_description = models.TextField(null=True)
    phone_number = models.IntegerField(null=True)
    telegram = models.CharField(max_length=50, null=True)
    instagram = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"
