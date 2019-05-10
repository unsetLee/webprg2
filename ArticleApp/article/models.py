from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=500, help_text='Enter a article content')
    author = models.CharField(max_length=10) #models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    create_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

