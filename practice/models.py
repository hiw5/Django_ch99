from django.db import models

# Create your models here.
class PracticeModels(models.Model):
    primary_key=models.AutoField("pk", db_column='pk', primary_key=True)
    practice_char=models.CharField("PRACTICE_CHAR", max_length=50, blank=True, null=True)
    practice_int=models.IntegerField("PRACTICE_INT", blank=True, null=True)
    practice_dt=models.DateTimeField("PRACTICE_DT", blank=True, null=True)

    def __str__(self):              # 생성자. Bookmark만 템플릿에서 호출시 title을 반환
        return str(self.primary_key)
    
    class Meta:
        verbose_name = 'practice_verbose_name'
        verbose_name_plural = 'practice_verbose_name_plural'
        db_table = 'practice_db_table'
