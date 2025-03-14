from django.urls import path
from practice.views import PracticeViews, PracticePaginationViews

app_name= "practice_app_name"

urlpatterns=[
    path("", PracticeViews.as_view(), name='practice_name'),
    path("pagination/", PracticePaginationViews.as_view(), name='practice_pagination'),
    #path("practice/get_con/", PracticeViews.as_view(view='get_con'), name='get_con'),
]