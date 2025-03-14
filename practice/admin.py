from django.contrib import admin
from practice.models import PracticeModels

# Register your models here.
@admin.register(PracticeModels)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('primary_key', 'practice_char', 'practice_int', 'practice_dt')