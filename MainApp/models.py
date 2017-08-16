from django.db import models
from .utils import code_generator
from django.conf import settings
# Create your models here.

SHORTCODE_MAX = getattr(settings,'SHORTCODE_MAX',15)

class URLManager(models.Manager):
    def refresh_shortcodes(self):
        changed=0
        qs=URL.objects.all()
        for q in qs:
            q.shortcode = code_generator()
            q.save()
            changed+=1
        return changed

class URL(models.Model):
    url = models.URLField(max_length=1024)
    shortcode =models.CharField(max_length=SHORTCODE_MAX,null=True,blank=True,unique=True)
    timestamp=models.DateTimeField(auto_now_add = False,auto_now = True)
    created = models.DateTimeField(auto_now_add=True , auto_now = False)
    

    objects = URLManager()

    def __str__(self):
        return str(self.url)

    def save(self,*args,**kwargs):
        if not self.shortcode:
            self.shortcode = code_generator()
        if not "http" in self.url:
            self.url= "http://" + self.url
        
        super(URL,self).save(*args,**kwargs)
