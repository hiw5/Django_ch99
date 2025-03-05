from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):              # Bookmark 생성자. Bookmark만 템플릿에서 호출시 title을 반환
        return self.title
    