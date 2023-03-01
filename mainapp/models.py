from django.db import models

class Photo(models.Model):
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.caption