from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    # unique is true = PK
    name = models.CharField(max_length=128, unique=True)
    slug= models.SlugField(unique=True)
    image= models.ImageField(null=True, blank=True)

    # overriding the save method and update slug field
    # everytime the category name changes, the slug will change
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    # for string representation
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=20000)
    technologies = models.CharField(max_length=500)
    url = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
