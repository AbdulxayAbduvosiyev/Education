from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Heshteg(models.Model):
    name_heshteg = models.CharField(max_length=50)
    
    def __str__(self):
     return self.name_heshteg
    
    
class Category(models.Model):
    name_category = models.CharField(max_length=50)
    
    def __str__(self):
       return self.name_category
   
   
   
class Blog(models.Model):
    title = models.CharField(max_length=250)
    banner_image = models.ImageField(upload_to='edu_images/')
    content = models.TextField()
    author_name = models.CharField(max_length=50)
    author_image = models.ImageField(upload_to='edu_images/')
    author_discriptions = models.TextField()
    heshteg = models.ManyToManyField(Heshteg, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug}) 
    
    def save(self, *args, **kwargs ):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args , **kwargs)
    

class Comment(models.Model):
    blog =  models.ForeignKey(Blog , on_delete=models.CASCADE,  null=True)
    name = models.CharField(max_length=50 , default="Unknown")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    