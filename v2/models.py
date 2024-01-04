import hashlib
from django.db import models

# Create your models here. 

from django.utils.deconstruct import deconstructible 

@deconstructible
class UploadPath (object):
    def __call__ (self, instance, filename):
        return hashname (filename) 

def hashname(ori_name): 
    return hashlib.md5(ori_name[:-4].encode("UTF-8")).hexdigest() + ".png" 

class Skin (models.Model): 
    file = models.ImageField() 
    model = models.CharField(max_length=30, default="geometry.humanoid.customSlim")
    name = models.CharField(max_length=30) 

    def __str__(self): 
        return self.name 

    def get_file(self): 
        return self.file 
    
class SkinList (models.Model): 
    skin = models.ManyToManyField(Skin, blank=True, related_name="cont") 
