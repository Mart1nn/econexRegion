from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    


class Category(models.Model):
    name = models.CharField(max_length=100)
    order_num = models.IntegerField()
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name

class Seria(models.Model):
    slug = models.SlugField(null=True, blank=True)
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    desc = models.CharField(max_length=500, blank=True, null=True)
    catogory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.catogory.name} {self.name}"

    

    def get_lm(self):
        if self.osveshmodel_set.count() != 0:
            mn = self.osveshmodel_set.order_by("light")[0].light
            mx = self.osveshmodel_set.order_by("light").last().light
        else:
            mn, mx = 0, 0
        return f"от {mn} лм до {mx} лм"

    def get_vt(self):
        if self.osveshmodel_set.count() != 0:
            mn = self.osveshmodel_set.order_by("power")[0].power
            mx = self.osveshmodel_set.order_by("power").last().power
        else:
            mn, mx = 0, 0
        return f"от {mn} вт до {mx} вт"

    

        


class OsveshModel(models.Model):
    name = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    power = models.IntegerField()
    light = models.IntegerField()
    efficincy = models.IntegerField()
    size = models.CharField(max_length=100)
    price = models.IntegerField()
    seria = models.ForeignKey(Seria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.seria.name} {self.name}"
    
   
