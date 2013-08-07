from django.db import models
import datetime

class Activity(models.Model):
    ActivityName = models.CharField(max_length=80)
    ActivityType= models.CharField(max_length=90)
    ActivityDate = models.DateField()
    ActivityDesc = models.CharField(max_length=180)
   
    def __unicode__(self):
        return self.ActivityName


#class PhoneNo(models.Model):
#    contact = models.ForeignKey(Contact)
#    phone_no = models.CharField(max_length=20)
#    phone_type = models.CharField(max_length=10)

#    def __unicode__(self):
#        return self.phone_no
