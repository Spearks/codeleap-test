from django.db import models

# Create your models here.

# Careers model used on API to store careers data
class Careers(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, blank=False, null=False)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=256, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ['created_datetime']