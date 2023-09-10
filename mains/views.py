from django.shortcuts import render
from .models import LangCategory, LevelTags


def index(r):

    tag = LevelTags.objects.all()
    ctx = {
        'tag': tag,
    }
    return render(r, 'mains/index.html', ctx)
