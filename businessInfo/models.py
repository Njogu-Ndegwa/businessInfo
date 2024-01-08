from django.db import models

class BusinessInfo(models.Model):
    business_name = models.CharField(max_length = 30)
    services_offered = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.CharField(max_length = 30)
    business_contact = models.CharField(max_length = 30)
    business_email = models.CharField(max_length = 30, blank=True)
    social_media_handle = models.CharField(max_length = 30)
    business_website = models.CharField(max_length = 30, blank=True)
    whatsup_link = models.CharField(max_length = 30, blank=True)
