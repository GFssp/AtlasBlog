from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)
    subtitle = models.CharField(max_length=200, blank=False)
    text = models.TextField(blank=False)
    pub_date = models.DateField(null=True, blank=False)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"id": self.id})

    def __str__(self):
        return f"{self.title}: {self.subtitle}"
    