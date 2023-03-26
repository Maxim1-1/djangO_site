from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    img = models.ImageField(upload_to='post/img')
    slug = models.SlugField(max_length=300, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

