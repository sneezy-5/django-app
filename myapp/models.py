from django.db import models

# Create your models here.

class Message(models.Model):

    nomPrenom = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    sujet = models.CharField(max_length=300)
    message = models.TextField(null=False)
    date =models.DateTimeField(auto_now_add=True)

    def __unicode__(self):


        return u"%s" % self.message
