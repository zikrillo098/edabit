from django.db import models
from client.models import User


class LangCategory(models.Model):
    LANGUAGE_CHOOSE = [
        ('Python', 'Python'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScripts'),
        ('PHP', 'PHP'),
        ('Python', 'Python'),
        ('Ruby', 'Ruby'),
        ('Swift', 'Swift')
    ]
    title = models.CharField(max_length=155, choices=LANGUAGE_CHOOSE, default='Python')
    objects = models.Manager()


class LevelTags(models.Model):
    TAGS_CHOOSE = [
        ('Hard', 'Hard'),
        ('Middle', 'Middle'),
        ('Easy', 'Easy'),
        ('Very Easy', 'Very Easy')
    ]
    category = models.ForeignKey(LangCategory, on_delete=models.CASCADE)
    tags = models.CharField(max_length=20, choices=TAGS_CHOOSE)
    objects = models.Manager()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(LangCategory, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
