from django.db import models
from django.utils import timezone

class Boast_Roast(models.Model):
    post_type = models.BooleanField()
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    content = models.CharField(max_length=280)
    date_created = models.DateTimeField(default=timezone.now)

