from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)
    subtitle = models.CharField(max_length=200, blank=False)
    text = models.TextField(blank=False)
    pub_date = models.DateField(null=True, blank=False)

    def __str__(self):
        return f"{self.title}: {self.subtitle}"
    