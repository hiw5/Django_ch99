from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
# Create your views here.


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):           # 명시적으로 처리해보기
    model = Bookmark
