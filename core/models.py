from django.db import models

class Request(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
      return self.title
# Create your models here.
