from django.db import models
from django.contrib import admin
from .models import DownloadLog

admin.site.register(DownloadLog)

class DownloadLog(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} at {self.timestamp}"
