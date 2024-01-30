from django.db import models
from django.utils import timezone

class ai_analysis_log(models.Model):
    image_path = models.CharField(max_length=255)
    success = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    class_id = models.IntegerField()
    confidence = models.FloatField()
    request_timestamp = models.DateTimeField("date published")
    response_timestamp = models.DateTimeField("date published")

    def __str__(self):
        return str(self.id) +' '+ self.image_path