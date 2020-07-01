from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    heaading = models.CharField(max_length=500)
    content = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.hea ading