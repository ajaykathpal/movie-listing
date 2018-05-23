from django.db import models

# Create your models here.
class Movies(models.Model):
    title=models.CharField(max_length=300)
    release_date = models.DateField()

    def get_listing(self):
        return self.objects.all()[:5]

